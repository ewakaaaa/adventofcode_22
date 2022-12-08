import os

elfs = []
sum_ = 0

with open(f"{os.getcwd()}/day01/puzzle.txt", "r") as file: 
    for line in file:
        if line.strip() != "":
            sum_ += int(line.strip())
        else: 
            elfs.append(sum_)
            sum_ = 0 
elfs.append(sum_)

#A
print(max(elfs))

#B 
print(sum(sorted(elfs,reverse=True)[:3]))