#!/usr/bin/python3
"""Python code that returns the perimeter where 0 is water and 1 is land"""


def island_perimeter(grid):
    """land is 1 and water is 0"""
    land = 1
    water = 0
    perimeter = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == land:
                # print("land in [x= {:d} y= {:d}]".format(x, y))
                # left
                if y == 0 or grid[y - 1][x] == water:
                    perimeter += 1
                # right
                if y == len(grid) - 1 or grid[y + 1][x] == water:
                    perimeter += 1
                # up
                if x == 0 or grid[y][x - 1] == water:
                    perimeter += 1
                # down
                if x == len(row) - 1 or grid[y][x + 1] == water:
                    perimeter += 1
    return perimeter
