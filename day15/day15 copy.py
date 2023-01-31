

import os 
from dataclasses import dataclass
file = open(f"{os.getcwd()}/day15/puzzle_test.txt", "r")
file = file.read() 

@dataclass
class Point:
    x: int 
    y: int 

@dataclass
class Line:
    a: int 
    b: int 

def manhattan(a,b):
    return abs(a.x-b.x) + abs(a.y-b.y)

def calculate_a_b(foo,bar):
    a = (foo.y - bar.y) / (foo.x-bar.x)
    b = foo.y - a*foo.x
    return Line(a,b)

def find_lines(c,r):
    return [calculate_a_b(Point(c.x,c.y+r),Point(c.x+r,c.y)), 
            calculate_a_b(Point(c.x+r,c.y),Point(c.x,c.y-r)),
            calculate_a_b(Point(c.x,c.y-r),Point(c.x-r,c.y)),
            calculate_a_b(Point(c.x,c.y+r),Point(c.x-3,c.y))] 

def read_point(string:str):
    x = int(string.split("x=")[1].split(",")[0])
    y = int(string.split("y=")[1])
    return Point(x,y)

for line in file.split("\n"):
    sensor, beacon = line.split(":")
    sensor = read_point(sensor)
    beacon = read_point(beacon)
    distanse = manhattan(sensor,beacon)
    find_lines(sensor,distanse)
    

