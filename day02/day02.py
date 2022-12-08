import os 

ruls = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3} 
points = 0 

with open(f"{os.getcwd()}/day02/puzzle.txt", "r") as file: 
    for line in file:
        opponent, me = line.strip().split(" ")
        if (ruls[me] - ruls[opponent] == 1) or (ruls[me] - ruls[opponent] == -2): 
            points += ruls[me] + 6 
        elif ruls[me] == ruls[opponent]:
            points += ruls[me] + 3 
        elif (ruls[me] - ruls[opponent] == 2) or (ruls[me] - ruls[opponent] == -1): 
            points += ruls[me]

# A 
print(points)

#B 
points = 0 
with open(f"{os.getcwd()}/day02/puzzle.txt", "r") as file: 
    for line in file:
        opponent, result = line.strip().split(" ")
        if result == "X":
            if ruls[opponent] - 1 > 0: 
                points += ruls[opponent] - 1  
            else: 
                points += 3 
        elif result == "Y":
            points += ruls[opponent] + 3 
        elif result == "Z": 
            if ruls[opponent] == 3: 
                points += 1 + 6 
            else: 
                points += ruls[opponent] + 1 + 6 

print(points)
