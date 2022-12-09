import os 
import math
from dataclasses import dataclass

@dataclass
class Point:
    x: int 
    y: int 

def move_head(H,direction):
    if direction == "R":
        H = Point(H.x+1,H.y)
    if direction == "L":
        H = Point(H.x-1,H.y)
    if direction == "D":
        H = Point(H.x,H.y-1)
    if direction == "U":
        H = Point(H.x,H.y+1)
    return H

def diagonal_move(H,T):
    row_distanse = T.x-H.x
    column_distanse = T.y-H.y
    if row_distanse < 0 and column_distanse < 0: 
        T = Point(T.x + 1, T.y + 1)
    if row_distanse > 0 and column_distanse > 0: 
        T = Point(T.x - 1 , T.y -1)
    if row_distanse > 0 and column_distanse < 0: 
        T = Point(T.x - 1 , T.y + 1)
    if row_distanse < 0 and column_distanse > 0:
        T = Point(T.x + 1 , T.y - 1) 
    return T 

def move_tail(H,T): 
    distanse = math.sqrt((H.x-T.x)**2 + (H.y-T.y)**2) 
    if distanse <= math.sqrt(2):
        pass #dont move 
    elif H.x == T.x: #this same row
        if H.y > T.y:
            T.y = T.y + 1 
        if H.y < T.y: 
            T.y = T.y - 1 
    elif H.y == T.y: #this same columns
        if H.x > T.x:
            T.x = T.x + 1 
        if H.x < T.x:
            T.x = T.x - 1  
    else: #diagonal 
        T = diagonal_move(H,T)
    return T

file = open(f"{os.getcwd()}/day09/puzzle.txt", "r") 
file = file.readlines()

# A 
H = Point(0,0)
T = Point(0,0)
tail_path = set()

for line in file:
    direction, moves = line.strip().split(" ")
    moves = int(moves)
    for i in range(0,moves):
        H = move_head(H,direction)
        T = move_tail(H,T)
        tail_path.add((T.x,T.y))

print(f"Part 1: {len(tail_path)}")

# B 
rope = []
for i in range(0,10): 
    rope.append(Point(0,0))

tail_path = set()

for line in file:
    direction, moves = line.strip().split(" ")
    moves = int(moves)
    for i in range(0,moves):
        rope[0] = move_head(rope[0],direction)
        for i in range(1,10):
            rope[i] = move_tail(rope[i-1], rope[i])
        tail_path.add((rope[9].x,rope[9].y))

print(f"Part 2: {len(tail_path)}")