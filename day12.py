from utils import read_input
import collections
import string

DAY = 12
TEST = False
def parse(input_str: str):
    return [list(row) for row in input_str.split("\n")]

def distance(start, grid):
    visited = set([start])
    q = collections.deque([(start[0], start[1], 0)])

    while q:
        i, j, d = q.popleft()
        
        if grid[i][j] == "E":
            return d 

        for ni, nj in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]): 
                if grid[ni][nj] == "E" and ord('z') - ord(grid[i][j]) <= 1:
                    q.append((ni, nj, d + 1))
                elif grid[ni][nj] != "E" and (ni, nj) not in visited and ord(grid[ni][nj]) - ord(grid[i][j]) <= 1:
                    visited.add((ni, nj))
                    q.append((ni, nj, d + 1))

def part1(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                grid[i][j] = "a"
                return distance((i, j), grid)
    

def part2(grid):
    res = float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S" or grid[i][j] == "a":
                grid[i][j] = "a"
                d = distance((i, j), grid)
                if d:
                    res = min(res, d)            
    return res

if __name__ == '__main__':
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
