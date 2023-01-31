import os
from dataclasses import dataclass

file = open(f"{os.getcwd()}/day15/puzzle.txt", "r")
file = file.read()


@dataclass
class Point:
    x: int
    y: int


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


# def genarate_all_points_in_squre(c,r):
#     points = set()
#     for x in range(c.x-r, c.x+r+1):
#         for y in range(c.y-r,c.y+r+1):
#             if manhattan(Point(x,y),c) <= r:
#                 points.add((x,y))

#     return points


def genarate_all_points_in_squre(c, r):
    points = set()
    y = 2000000
    for x in range(c.x - r, c.x + r + 1):
        if manhattan(Point(x, y), c) <= r:
            points.add((x, y))

    return points


# print(genarate_all_points_in_squre(Point(0,0),1))


def read_point(string: str):
    x = int(string.split("x=")[1].split(",")[0])
    y = int(string.split("y=")[1])
    return Point(x, y)


points_without_lighthous = set()
for line in file.split("\n"):
    sensor, beacon = line.split(":")
    sensor = read_point(sensor)
    beacon = read_point(beacon)
    points_without_lighthous_for_line = genarate_all_points_in_squre(
        sensor, manhattan(sensor, beacon)
    )
    points_without_lighthous_for_line.discard((beacon.x, beacon.y))
    points_without_lighthous = (
        points_without_lighthous | points_without_lighthous_for_line
    )

print(len(points_without_lighthous))
