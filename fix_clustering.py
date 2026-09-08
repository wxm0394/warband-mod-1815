import math

PARTIES_FILE = "parties.txt"
BACKUP_FILE = "parties.txt.backup_clustering"

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Read all parties
with open(PARTIES_FILE, "r") as f:
    lines = f.readlines()

import shutil
shutil.copy(PARTIES_FILE, BACKUP_FILE)

deleted_names = {"Lovie", "Cont", "Dozingem", "Couthof"}

new_lines = []
centers = []

# Parse
for i, line in enumerate(lines):
    parts = line.strip().split()
    if len(parts) >= 16 and (parts[0] == "1" and parts[3].startswith("p_")):
        name = parts[4] # The human readable name is parts[4]
        is_center = "p_town_" in parts[3] or "p_castle_" in parts[3] or "p_village_" in parts[3]
        
        if is_center and name not in {"Zendar", "Main_Party", "Lille", "Brussel", "Cassel"}:
            x = float(parts[-8])
            y = float(parts[-7])
            
            if name in deleted_names:
                # Move to corner
                x, y = 175.0, 175.0
            
            centers.append({
                "index": i,
                "name": name,
                "x": x,
                "y": y,
                "deleted": name in deleted_names
            })

print(f"Loaded {len(centers)} static centers for physics calculation.")

# Physics simulation to push overlapping non-deleted centers apart
MIN_DIST = 4.5
ITERATIONS = 100

for _ in range(ITERATIONS):
    displacements = {c["index"]: [0.0, 0.0] for c in centers}
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            c1 = centers[i]
            c2 = centers[j]
            if c1["deleted"] or c2["deleted"]: continue
            
            dist = distance(c1["x"], c1["y"], c2["x"], c2["y"])
            if dist < MIN_DIST and dist > 0:
                overlap = MIN_DIST - dist
                dx = (c1["x"] - c2["x"]) / dist
                dy = (c1["y"] - c2["y"]) / dist
                
                displacements[c1["index"]][0] += dx * overlap * 0.5
                displacements[c1["index"]][1] += dy * overlap * 0.5
                displacements[c2["index"]][0] -= dx * overlap * 0.5
                displacements[c2["index"]][1] -= dy * overlap * 0.5
            elif dist == 0:
                displacements[c1["index"]][0] += 0.5
                displacements[c2["index"]][0] -= 0.5

    moved = False
    for c in centers:
        if not c["deleted"]:
            dx, dy = displacements[c["index"]]
            if abs(dx) > 0.01 or abs(dy) > 0.01:
                moved = True
                c["x"] += dx * 0.1
                c["y"] += dy * 0.1
    if not moved:
        break

# Update lines
for c in centers:
    idx = c["index"]
    
    # We will use regex replacement so we preserve whitespace precisely
    import re
    line = lines[idx]
    gx, gy = c["x"], c["y"]
    coord_pattern = r"([\-\d\.]+\s+[\-\d\.]+\s+[\-\d\.]+\s+[\-\d\.]+\s+[\-\d\.]+\s+[\-\d\.]+)(\s+0\.0\s+\d+\s*)$"
    new_coord_str = f"{gx:.6f} {gy:.6f} {gx:.6f} {gy:.6f} {gx:.6f} {gy:.6f}"
    
    # Check if the regex matches, and perform the substitution
    lines[idx] = re.sub(coord_pattern, new_coord_str + r"\2", line)

with open(PARTIES_FILE, "w") as f:
    f.writelines(lines)

print("Coordinates adjusted. Deleted items moved to 175, 175.")
