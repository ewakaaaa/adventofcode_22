import os 
import re

file = open(f"{os.getcwd()}/day05/puzzle_stos.txt", "r")
file = file.readlines()

stos = {k:[] for k in range(1,10)}
for i in file:
    for e, s in enumerate(range(1,len(i),4)): 
        if i[s] != " ": 
            stos[e+1].append(i[s])      

file = open(f"{os.getcwd()}/day05/puzzle_move.txt", "r")
file = file.readlines()

# A 
for line in file: 
    move,from_,to = [int(i) for i in re.findall(r'\d+', line)] 
    for steps in range(0,int(move)):
        stos[to].insert(0, stos[from_][0])
        stos[from_].pop(0)


# B 
file = open(f"{os.getcwd()}/day05/puzzle_stos.txt", "r")
file = file.readlines()

stos = {k:[] for k in range(1,10)}
for i in file:
    for e, s in enumerate(range(1,len(i),4)): 
        if i[s] != " ": 
            stos[e+1].append(i[s])      

file = open(f"{os.getcwd()}/day05/puzzle_move.txt", "r")
file = file.readlines()

for line in file: 
    move,from_,to = [int(i) for i in re.findall(r'\d+', line)] 
    stos[to][:0] = stos[from_][0:move]
    for steps in range(0,move):
        stos[from_].pop(0)

for i in range(1,10):
    print(stos[i][0])