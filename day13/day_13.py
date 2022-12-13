import os 
from functools import cmp_to_key

def compare(left,right):
    for l,r in zip(left,right):
        if isinstance(l,int) and isinstance(r,int):
            if l<r:
                return 1 
            elif l>r:
                return -1
            else: 
                pass
        elif isinstance(l,list) and isinstance(r,list):
            result = compare(l,r)
            if isinstance(result,int): 
                return result
        elif isinstance(l,list) and isinstance(r,int):
            r = [r]
            result = compare(l,r)
            if isinstance(result,int): 
                return result
        elif isinstance(l,int) and isinstance(r,list):
            l = [l]
            result = compare(l,r)
            if isinstance(result,int): 
                return result
    if len(left) < len(right):
        return 1
    if len(left) > len(right):
        return -1

file = open(f"{os.getcwd()}/day13/puzzle.txt", "r") 
file = file.read()

sum_ = 0 
for i,p in enumerate(file.split("\n\n")): 
    left, right = p.split("\n")
    if compare(eval(left),eval(right)) == 1: 
        sum_ = sum_ + i + 1 

print(f"Part 1: {sum_}")

file = [eval(f) for f in file.split("\n") if f != ""]
file.append([[2]])
file.append([[6]])

multiple = [] 
sorted_result = sorted(file, key=cmp_to_key(compare),reverse=True) 
for i,value in enumerate(sorted_result): 
    if (value == [[2]]) or (value == [[6]]):
        multiple.append(i+1)

print(f"Part 2: {multiple[0]*multiple[1]}")
