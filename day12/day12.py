import os
import numpy as np
from dijkstra import *
import string

alphabet = list(string.ascii_lowercase)
alphabet = {k: v for k, v in zip(alphabet, range(0, len(alphabet) + 1))}
alphabet["S"] = -1
alphabet["E"] = 26

# reading data
file = open(f"{os.getcwd()}/day12/puzzle.txt", "r")
map = []
for i, line in enumerate(file):
    row = [alphabet[item] for item in line.strip()]
    map.append(row)
    for j, item in enumerate(line.strip()):
        if item == "E":
            end = (i, j)
    for j, item in enumerate(line.strip()):
        if item == "S":
            start = (i, j)

map = np.array(map)

# creating a graph of connections between points
graph = {}
for row in range(0, map.shape[0]):
    for col in range(0, map.shape[1]):
        graph[(row, col)] = {}
        value = map[row][col]
        if row != map.shape[0] - 1:
            if map[row + 1][col] <= value + 1:
                graph[(row, col)][(row + 1, col)] = 1
        if col != map.shape[1] - 1:
            if map[row][col + 1] <= value + 1:
                graph[(row, col)][(row, col + 1)] = 1
        if row != 0:
            if map[row - 1][col] <= value + 1:
                graph[(row, col)][(row - 1, col)] = 1
        if col != 0:
            if map[row][col - 1] <= value + 1:
                graph[(row, col)][(row, col - 1)] = 1
        if (row, col) == end:
            graph[end] = {}

# can't go to start:
for k, v in graph.items():
    v.pop(start, None)

cost = dijksta(graph, start, end)
print(f"Part 1: {cost}")

start_points = [start]
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == 0:
            start_points.append((i, j))

costs = []
for start in start_points:
    for k, v in graph.items():
        v.pop(start, None)
    cost = dijksta(graph, start, end)
    costs.append(cost)

print(f"Part 2: {min(costs)}")
