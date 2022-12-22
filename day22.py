from utils import read_input
import re
DAY = 22
TEST = False

input_str = read_input(day=DAY, test=TEST)


a, b = input_str.split('\n\n')
grid = a.splitlines()
sequence = re.findall(r'\d+|[RL]', b)

width = max(map(len, grid))
grid = [line + " " * (width - len(line)) for line in grid]

# initialize start position
for i, char in enumerate(grid[0]):
    if char == '.':
        r = 0
        c = i
        dr = 0
        dc = 1
        break


for inst in sequence:
    if inst == 'R':
        dr, dc = dc, -dr
    elif inst == 'L':
        dr, dc = -dc, dr
    else:
        for _ in range(int(inst)):
            cdr = dr
            cdc = dc
            nr = r + dr
            nc = c + dc
            if nr < 0 and 50 <= nc < 100 and dr == -1:
                dr, dc = 0, 1
                nr, nc = nc + 100, 0
            elif nc < 0 and 150 <= nr < 200 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 0, nr - 100
            elif nr < 0 and 100 <= nc < 150 and dr == -1:
                nr, nc = 199, nc - 100
            elif nr >= 200 and 0 <= nc < 50 and dr == 1:
                nr, nc = 0, nc + 100
            elif nc >= 150 and 0 <= nr < 50 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 99
            elif nc == 100 and 100 <= nr < 150 and dc == 1:
                dc = -1
                nr, nc = 149 - nr, 149
            elif nr == 50 and 100 <= nc < 150 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc - 50, 99
            elif nc == 100 and 50 <= nr < 100 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 49, nr + 50
            elif nr == 150 and 50 <= nc < 100 and dr == 1:
                dr, dc = 0, -1
                nr, nc = nc + 100, 49
            elif nc == 50 and 150 <= nr < 200 and dc == 1:
                dr, dc = -1, 0
                nr, nc = 149, nr - 100
            elif nr == 99 and 0 <= nc < 50 and dr == -1:
                dr, dc = 0, 1
                nr, nc = nc + 50, 50
            elif nc == 49 and 50 <= nr < 100 and dc == -1:
                dr, dc = 1, 0
                nr, nc = 100, nr - 50
            elif nc == 49 and 0 <= nr < 50 and dc == -1:
                dc = 1
                nr, nc = 149 - nr, 0
            elif nc < 0 and 100 <= nr < 150 and dc == -1:
                dc = 1
                nr, nc = 149 - nr, 50
            print(nr, nc)
            if grid[nr][nc] == '#':
                dr = cdr
                dc = cdc
                break
            r = nr
            c = nc

dirs = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3,
}

print((r+1)*1000 + (c+1)*4 + dirs[(dr, dc)])
