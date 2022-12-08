import os 
import numpy as np 
file = open(f"{os.getcwd()}/day08/puzzle_test.txt", "r") 
file = file.readlines()

map = []
for row in file:
    row = [int(i) for i in row.strip()]
    map.append(row)

map = np.array(map) 
max_col,max_row = map.shape

# A 
count = 2 * (max_col + max_row -2 ) 
for row in range(1, map.shape[0] - 1):
    for col in range(1, map.shape[1] - 1):
        point = map[row][col]
        smaller_tree = 0
        for vector in [map[row+1:max_row,col], map[0:row,col], map[row,0:col], map[row,col+1:max_col]]:
            if all(vector<point):
                count +=1
                break
print(count)

# B 
def count_tree(vector,point): 
    count = 1 
    for i in range(0,len(vector)-1): 
        if vector[i] < point: 
            count += 1 
        else: 
            break
    return count 

scenic_scores = [] 
for row in range(0, map.shape[0]):
    for col in range(0, map.shape[1]):
        point = map[row][col]
        seen_tree = []
        for vector in (map[row+1:max_row,col], np.flip(map[0:row,col]),np.flip(map[row,0:col]),map[row,col+1:max_col]): 
            seen_tree.append(count_tree(vector,point))
        scenic_scores.append(np.prod(seen_tree)) 

print(max(scenic_scores))


