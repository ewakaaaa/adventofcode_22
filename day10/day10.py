import os 

file = open(f"{os.getcwd()}/day10/puzzle.txt", "r") 
file = file.readlines()

# A 
X = 1
cycle = []

for line in file:
    line = line.strip()
    if line.startswith("addx"):
        name, value = line.split(" ")
        for i in range(0,2):
            cycle.append(X)
        X = X + int(value)
    else: 
        cycle.append(X)

strenght = 0
for i in [20, 60, 100, 140, 180, 220]:
    strenght = strenght + cycle[i-1]*(i)

print(f"Part 1: {strenght}")

# B 
draw = [] 
for i,value in enumerate(cycle):
    if (i+1)%40 in [value,value+1,value+2]:
        draw.append("#")
    else: 
        draw.append(".")

print("Part 2:")
for i in range(0,len(draw),40):
    line = " ".join(draw[i:i+40])
    print(line)