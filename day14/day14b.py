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
    x = int(x)
    y = int(y)
    return Point(x,y)

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
y_shape = max([y.y for y in rocks]) + 3

map = np.zeros((y_shape,x_shape))
for rock in rocks:
    map[rock.y][rock.x-min_x] = 1

for i in range(0,x_shape): 
    map[y_shape-1][i] = 1 

def sand_move(sand_p,map,start_sand_y):
    if sand_p.y+1 == map.shape[1]:
        new_y = np.zeros(y_shape) 
        new_y[y_shape-1] = 1 
        map = np.c_[map,new_y]
        start_sand_y = start_sand_y 
        sand_p = Point(sand_p.x, sand_p.y)
    if sand_p.y-1 == -1: 
        new_y = np.zeros(y_shape) 
        new_y[y_shape-1] = 1 
        map = np.c_[new_y,map]
        start_sand_y = start_sand_y + 1 
        sand_p = Point(sand_p.x, sand_p.y+1)
    # print(sand_p.x+1)
    if map[sand_p.x+1][sand_p.y] == 0: #dół 
        return (Point(sand_p.x+1,sand_p.y) ,map , start_sand_y)
    if map[sand_p.x+1][sand_p.y-1] == 0: #dól lewo 
        return (Point(sand_p.x+1,sand_p.y-1), map, start_sand_y)
    if map[sand_p.x+1][sand_p.y+1] == 0: #dół prawo 
        return (Point(sand_p.x+1,sand_p.y+1),map, start_sand_y)
    return None

start_sand_y = 500-min_x
start_sand_x = 0
sand_position = Point(start_sand_x,start_sand_y)
map = map 
for s in range(1,100): 

    while sand_move(sand_position,map,start_sand_y) is not None: 
        sand_position,map,start_sand_y = sand_move(sand_position,map,start_sand_y) 
        result = s
    
    map[sand_position.x][sand_position.y] = 9 
    sand_position = Point(start_sand_x,start_sand_y)

print(result)
