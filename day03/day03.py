import os 
import string
file = open(f"{os.getcwd()}/day03/puzzle.txt", "r")
file = file.readlines()

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
alphabet = {k:v for k,v in zip(alphabet,range(1,len(alphabet)+1))}

# A 
sum = 0 
for line in file:
    line = line.strip()
    half = int(len(line)/2)
    part_1 = set(line[0:half])
    part_2  = set(line[half:len(line)]) 
    value = part_1.intersection(part_2) 
    sum += alphabet[list(value)[0]]

print(sum)

# B 
sum = 0 
for i in range(0,len(file),3):
    tripels = [set(i.strip()) for i in file[i:i+3]] 
    value = tripels[0].intersection(tripels[1]).intersection(tripels[2])
    sum += alphabet[list(value)[0]]

print(sum)
