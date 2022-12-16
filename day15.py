from utils import read_input
from collections import defaultdict, deque

DAY = 15
TEST = False


def display(startx, endx, starty, endy):
    for y in range(starty, endy+1):
        print("{:02d}".format(y), end=' ')
        for x in range(startx, endx+1):
            print(grid[(x, y)], end='')
        print()
    print()


def in_manhattan(x, y, d):
    # paints all points within a certain points manhattan distance
    # I know this is inefficient but I'm not very smart
    queue = deque([(x, y)])
    visited = set()
    visited.add((x, y))
    while queue:
        xx, yy = queue.popleft()
        for xxx, yyy in [[xx, yy+1], [xx+1, yy], [xx, yy-1], [xx-1, yy]]:
            if (xxx, yyy) in visited: continue
            if manhattan(x, y, xxx, yyy) < d:
                queue.append((xxx, yyy))
            visited.add((xxx, yyy))
            if grid[(xxx, yyy)] == '.':
                grid[(xxx, yyy)] = '#'
        


def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


input_str = read_input(day=DAY, test=TEST)
grid = defaultdict(lambda: '.')
for line in input_str.split('\n'):
    l = line.split(' ')
    sx = int(l[2][2:-1])
    sy = int(l[3][2:-1])
    bx = int(l[8][2:-1])
    by = int(l[9][2:])
    mh = manhattan(sx, sy, bx, by)
    for dy, dx in ((-mh, 0),(mh, -0)):
        cy = sy + dy
        
    grid[(sx, sy)] = 'S'
    grid[(bx, by)] = 'B'
    
    in_manhattan(sx, sy, dist)
    display(-2, 25, 0, 22)
    
counter = 0
for x in range(-1000,1000):
    if grid[(x,10)] != '.':
        counter+=1
print(counter)



def part2(grid):
    pass
