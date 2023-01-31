import os
file = open(f"{os.getcwd()}/day20/puzzle_test.txt", "r")
file = file.read()
file = file.split("\n")
file = [int(i) for i in file]

orginal_file = file.copy()
size = len(orginal_file)
print(orginal_file)

for item in orginal_file: 
    print(item)
    current_index_of_item = file.index(item)
    if item > 0: 
        new_index = (current_index_of_item+item)
        if new_index > len(orginal_file): 
            new_index = new_index%len(orginal_file) + 1 
        file.pop(current_index_of_item)
        file.insert(new_index,item)
    elif item < 0: 
        new_index = (current_index_of_item + item -1 )%len(orginal_file)
        file.pop(current_index_of_item) 
        file.insert(new_index,item)
    else: 
        pass #don't move 
    print(file)


print(1000%size)