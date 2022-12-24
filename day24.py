import math
from utils import read_input
from collections import deque

DAY = 24
TEST = False
input_str = read_input(day=DAY, test=TEST)

blizzards = tuple(set() for _ in range(4))

for r, line in enumerate(input_str.splitlines()[1:]):
    for c, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((r, c))

queue = deque([(0, -1, 0, 0)])
seen = set()
targets = [(r, c - 1), (-1, 0)]

lcm = math.lcm(r, c)
part1 = True
while queue:
    time, cr, cc, stage = queue.popleft()
    
    time += 1

    for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
        nr = cr + dr
        nc = cc + dc
        
        nstage = stage

        
        if (nr, nc) == targets[stage % 2]:
            if part1 and stage == 0:
                print(time)
                part1 = False
            if stage == 2:
                print(time)
                exit(0)
            nstage += 1
        
        if (nr < 0 or nc < 0 or nr >= r or nc >= c) and (nr, nc) not in targets:
            continue
        
        fail = False
        
        if (nr, nc) not in targets:
            for i, (tr, tc) in enumerate(((0, -1), (0, 1), (-1, 0), (1, 0))):
                if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
                    fail = True
                    break
        
        if not fail:
            key = (nr, nc, nstage, time % lcm)
            
            if key in seen:
                continue

            seen.add(key)
            queue.append((time, nr, nc, nstage))