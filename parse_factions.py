with open("scripts.txt", "r") as f:
    lines = f.readlines()

game_start_line = lines[3] # Index 3 (4th line)
ops = game_start_line.strip().split()

print("Found", len(ops), "tokens in game_start")

for i in range(len(ops)):
    if ops[i] == '1': # call_script
        if i+4 < len(ops) and ops[i+1] == '3' and ops[i+2].startswith('93674872249306'):
            # give_center_to_faction_aux takes center and faction
            print("Assign:", ops[i+3], "->", ops[i+4])
