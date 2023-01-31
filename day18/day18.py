
import os
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class Cube:
    x: int
    y: int 
    z: int 

SIZE = 30

x, y, z = np.indices((SIZE, SIZE, SIZE))
cube1 = (x <= 2) & (y <= 1) & (z <= 1) & (1 < x ) & (0<y) & (0<z) 
cube2 = (x <= 1) & (y <= 1) & (z <= 1) & (0 < x ) & (0<y) & (0<z) 
voxelarray = cube1 | cube2 

visible_walls = 0 
for x in range (0,SIZE):
    for y in range(0,SIZE):
        for z in range(0,SIZE):
            if voxelarray[x][y][z]:
                visible_walls += (sum([~voxelarray[x-1][y][z],~voxelarray[x+1][y][z],~voxelarray[x][y+1][z],~voxelarray[x][y-1][z],~voxelarray[x][y][z+1],~voxelarray[x][y][z-1]]))

print(visible_walls)

# ax = plt.figure().add_subplot(projection='3d')
# ax.voxels(voxelarray, edgecolor='k')

# plt.show()

file = open(f"{os.getcwd()}/day18/puzzle_test.txt", "r")
file = file.read()
x, y, z = np.indices((SIZE, SIZE, SIZE))
voxelarray = (x < 0) & (y < 0) & (z <0)  

for cube in file.split("\n"): 
    x_,y_,z_ = cube.split(",")
    cube = Cube(int(x_),int(y_),int(z_))
    cube = (x <= cube.x) & (y <= cube.y) & (z <= cube.z) & (cube.x-1<x) & (cube.y-1<y) & (cube.z-1<z)
    voxelarray = cube | voxelarray

# ax = plt.figure().add_subplot(projection='3d')
# ax.voxels(voxelarray, edgecolor='k')
# plt.show()

visible_walls = 0 
for x in range (0,SIZE):
    for y in range(0,SIZE):
        for z in range(0,SIZE):
            if voxelarray[x][y][z]:
                visible_walls += (sum([~voxelarray[x-1][y][z],~voxelarray[x+1][y][z],~voxelarray[x][y+1][z],~voxelarray[x][y-1][z],~voxelarray[x][y][z+1],~voxelarray[x][y][z-1]]))

print(visible_walls)