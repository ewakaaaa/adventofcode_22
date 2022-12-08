import os 
file = open(f"{os.getcwd()}/day06/puzzle.txt", "r")
file = file.readlines()[0]

# A 
def get_first_index_of_unique_four(file): 
    four = []
    for i,s in enumerate(file): 
        if i < 4:
            four.append(s)
        if len(set(four)) == 4: 
            return i 
        four.append(s)
        four.pop(0)

print(get_first_index_of_unique_four(file))

# B 
def get_first_index_of_unique_four(file): 
    four = []
    for i,s in enumerate(file): 
        if i < 14:
            four.append(s)
        if len(set(four)) == 14: 
            return i 
        four.append(s)
        four.pop(0)

print(get_first_index_of_unique_four(file))