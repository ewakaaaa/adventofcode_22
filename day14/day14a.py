import os 
import sys
import numpy as np 
np.set_printoptions(threshold=sys.maxsize)
from dataclasses import dataclass
file = open(f"{os.getcwd()}/day14/puzzle_test.txt", "r")
file = file.read() 

@dataclass
class Point:
    x: int 
    y: int 

def read_point(item:list):
    x,y = item
    return Point(int(x),int(y))

# read data
rocks = []
for line in file.split("\n"):
    points = [p.split(",") for p in line.split(" -> ")]
    start = read_point(points[0])
    for p in points[1:]:
        p = read_point(p)
        if start.x == p.x: 
            if start.y < p.y: 
                for i in range(start.y,p.y+1):
                    rocks.append(Point(start.x,i))
            else: 
                for i in range(p.y,start.y+1):
                    rocks.append(Point(start.x,i))
        if start.y == p.y: 
            if start.x < p.x:
                for i in range(start.x,p.x+1):
                    rocks.append(Point(i,start.y))
            else: 
                for i in range(p.x,start.x+1):
                    rocks.append(Point(i,start.y))
        start = p 

min_x = min([x.x for x in rocks])
x_shape = max([x.x for x in rocks]) - min_x +1 
y_shape = max([y.y for y in rocks]) + 1

map = np.zeros((y_shape,x_shape))
for rock in rocks:
    map[rock.y][rock.x-min_x] = 1

# single step of movement of sand
def move_sand(sand_p):
    if map[sand_p.x+1][sand_p.y] == 0: 
        return Point(sand_p.x+1,sand_p.y)
    if map[sand_p.x+1][sand_p.y-1] == 0:
         return Point(sand_p.x+1,sand_p.y-1)
    if map[sand_p.x+1][sand_p.y+1] == 0:
         return Point(sand_p.x+1,sand_p.y+1)
    return None 

# sand motion simulation
for step in range(0,1000): 
    try: 
        start_point_of_sand = Point(0,500-min_x)
        while move_sand(start_point_of_sand) is not None: 
            start_point_of_sand = move_sand(start_point_of_sand) 
        map[start_point_of_sand.x][start_point_of_sand.y] = 9 
    except: 
        print(f"Part 1: {step}")
        break

# create new map with level of rocks 
map = np.zeros((y_shape+2,x_shape))
for rock in rocks:
    map[rock.y][rock.x-min_x] = 1

for i in range(0,x_shape): 
    map[y_shape+2-1][i] = 1 

# print map 
def print_map(map):
    map_int_to_string = {0:".",1:"#",9:"o"}
    for row in map:
        print(''.join([map_int_to_string[i] for i in row]))

# extend map to inf 
def extend_map_to_inf (map,current_ponit,start_point_of_sand):
    if current_ponit.y+1 == map.shape[1]:
        new_columns = np.zeros(map.shape[0]) 
        new_columns[map.shape[0]-1] = 1 
        map = np.c_[map,new_columns]
    if current_ponit.y-1 == -1: 
        new_columns = np.zeros(map.shape[0]) 
        new_columns[map.shape[0]-1] = 1 
        map = np.c_[new_columns,map]
        start_point_of_sand = Point(start_point_of_sand.x,start_point_of_sand.y+1)
        current_ponit = Point(current_ponit.x,current_ponit.y+1)
    return (map,current_ponit,start_point_of_sand)


start_point_of_sand = Point(0,500-min_x) 
current_ponit = start_point_of_sand
for s in range(1,100): 
    while move_sand(current_ponit) is not None: 
        map,current_ponit,start_point_of_sand = extend_map_to_inf(map,current_ponit,start_point_of_sand)
        current_ponit = move_sand(current_ponit)
        print(map.shape)
        print(current_ponit)
        result = s
    map[current_ponit.x][current_ponit.y] = 9 
    current_ponit = start_point_of_sand

print(f"Part 2: {result}")

