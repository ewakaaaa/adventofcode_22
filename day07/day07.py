import os 
file = open(f"{os.getcwd()}/day07/puzzle_test.txt", "r") 
file = file.readlines()

from os import path
from collections import defaultdict

system = defaultdict(int)
print(system)
path = []
for line in file:
    line = line.strip().split(" ")
    if len(line) == 3: 
        if line[2] == '..': 
            path.pop()
        else: 
            path.append(line[2])
    elif len(line) == 2: 
        if line[0] == '$':
            continue
        else: 
            try:
                system["/".join(path)] += int(line[0])
            except ValueError:
                pass



print(sum(s for s in system.values() if s <= 100000))


