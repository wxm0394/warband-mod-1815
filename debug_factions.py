import math

PARTIES_FILE = "parties.txt"
SCRIPTS_FILE = "scripts.txt"

party_coords = {}
with open(PARTIES_FILE, "r") as f:
    for i, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) >= 16 and (parts[0] == "1" and parts[4].startswith("p_")):
            party_coords[i] = (float(parts[-7]), float(parts[-6]))
print(f"Loaded {len(party_coords)} parties.")

with open(SCRIPTS_FILE, "r") as f:
    ops = f.readlines()[3].strip().split()

for i in range(len(ops)):
    if ops[i] == '1': 
        if i+4 < len(ops) and ops[i+1] == '3' and ops[i+2].startswith('93674872249306'):
            center_val = int(ops[i+3])
            if center_val >= 648518346341351424:
                p_idx = center_val - 648518346341351424
                if p_idx in party_coords:
                    print(f"Found center {p_idx} at {party_coords[p_idx]}, old fac: {ops[i+4]}")
                else:
                    print(f"Center {p_idx} not in party_coords!")
            else:
                print(f"Center val {center_val} not >= mask")
            break
