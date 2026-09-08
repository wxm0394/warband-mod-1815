import math

PARTIES_FILE = "parties.txt"
SCRIPTS_FILE = "scripts.txt"

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# 1. Read party coordinates
party_coords = {}
with open(PARTIES_FILE, "r") as f:
    for i, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) >= 16 and (parts[0] == "1" and parts[4].startswith("p_")):
            x = float(parts[-7])
            y = float(parts[-6])
            party_coords[i] = (x, y)

# Define anchors based on the factions
# France (633), Prussia (634), Britain (635), Netherlands (636), German Alliance (637), Habsburg (638)
anchors = {
    "633": [(-55, -25), (0, -25), (-10, -40)], # France
    "634": [(25, -20), (20, 5), (45, -10)], # Prussia
    "635": [(14, -2), (-50, 20), (-40, -15)], # Britain
    "636": [(10, 30), (-20, 25), (20, 50)], # Netherlands
    "637": [(50, 0), (65, 5), (65, -25), (75, -40)], # German Alliance
    "638": [(45, -50), (55, -45)] # Habsburg
}

def get_faction(x, y):
    best_fac = "633"
    min_dist = 999999.0
    for fac, pts in anchors.items():
        for px, py in pts:
            dist = distance(x, y, px, py)
            if dist < min_dist:
                min_dist = dist
                best_fac = fac
    return "432345564227567" + best_fac

# 2. Modify scripts.txt
with open(SCRIPTS_FILE, "r") as f:
    lines = f.readlines()

import shutil
shutil.copy(SCRIPTS_FILE, SCRIPTS_FILE + ".backup2")

game_start_line = lines[3]
ops = game_start_line.strip().split()

changes = 0
for i in range(len(ops)):
    if ops[i] == '1': # call_script
        if i+4 < len(ops) and ops[i+1] == '3' and ops[i+2].startswith('93674872249306'):
            center_val = int(ops[i+3])
            # The mask for party is 648518346341351424
            if center_val >= 648518346341351424:
                p_idx = center_val - 648518346341351424
                if p_idx in party_coords:
                    x, y = party_coords[p_idx]
                    new_fac = get_faction(x, y)
                    old_fac = ops[i+4]
                    if new_fac != old_fac:
                        ops[i+4] = new_fac
                        changes += 1

lines[3] = " " + " ".join(ops) + " \n"

with open(SCRIPTS_FILE, "w") as f:
    f.writelines(lines)

print(f"Faction reassignment complete. {changes} centers updated.")
