import os 

# A 
sum_ = 0 
with open(f"{os.getcwd()}/day04/puzzle.txt", "r") as file: 
    for line in file:
        first, second = ([i.split("-") for i in line.strip().split(",")])
        first = set(range(int(first[0]),int(first[1])+1))
        second = set(range(int(second[0]),int(second[1])+1))
        if first <= second or first >= second:
            sum_ += 1
print(sum_)

# B 
sum_ = 0 
with open(f"{os.getcwd()}/day04/puzzle.txt", "r") as file: 
    for line in file:
        first, second = ([i.split("-") for i in line.strip().split(",")])
        first = set(range(int(first[0]),int(first[1])+1))
        second = set(range(int(second[0]),int(second[1])+1))
        if first.intersection(second):
            sum_ += 1
print(sum_)