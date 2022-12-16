from utils import read_input
from collections import defaultdict
import numpy as np

DAY = 14
TEST = False


def parse(input_str: str):
    grid = defaultdict(lambda: '.')
    coordsList = [[tuple(map(int, pair.split(',')))
                   for pair in line.split(' -> ')] for line in input_str.split('\n')]

    for coords in coordsList:
        for (a, b), (c, d) in zip(coords, coords[1:]):
            for i in range(min(a, c), max(a, c)+1):
                for j in range(min(b, d), max(b, d)+1):
                    grid[(i, j)] = '#'
    return grid


def part1(grid):
    voidLimit = max(map(lambda x: x[1], grid.keys()))

    def move(x, y, grid):
        for ii, jj in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
            if grid[(ii, jj)] not in 'o#':
                return ii, jj
        return x, y

    startx, starty = 500, 0
    prev = (startx, starty)
    while True:
        new = move(*prev, grid)
        if new == prev:
            # if sand is stopped
            grid[new] = 'o'
            prev = (startx, starty)
        else:
            # if sand flowing
            if new[1]>voidLimit:
                break
            prev = new

    return len([x for x in grid.values() if x == 'o'])



def part2(grid):
    floor = max(map(lambda x: x[1], grid.keys())) + 2

    def move(x, y, grid):
        for ii, jj in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
            if grid[(ii, jj)] not in 'o#' and jj != floor:
                return ii, jj
        return x, y

    startx, starty = 500, 0
    prev = (startx, starty)
    while True:
        new = move(*prev, grid)
        if new == prev:
            # if sand is stopped
            grid[new] = 'o'
            prev = (startx, starty)

            if new == (startx, starty):
                # if sand blocks source
                break
        else:
            # if sand flowing
            if new[1]>floor:
                break
            prev = new

    return len([x for x in grid.values() if x == 'o'])


def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    data = parse(input_str)
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
