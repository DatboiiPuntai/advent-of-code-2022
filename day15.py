from utils import read_input
import re

DAY = 15
TEST = False

def dist(sx, sy, bx, by):
        return abs(sx - bx) + abs(sy - by)

def part1():
    Y = 10 if TEST else 2000000

    known = set()
    intervals = []

    input_str = read_input(day=DAY, test=TEST)
    for line in input_str.splitlines():
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        d = dist(sx, sy, bx, by)
        o = d - abs(sy - Y)

        if o < 0:
            continue

        lx = sx - o
        hx = sx + o
        intervals.append([lx, hx])

        if by == Y:
            known.add(bx)

    intervals.sort()

    q = []
    for lo, hi in intervals:
        if not q:
            q.append([lo, hi])
            continue

        qlo, qhi = q[-1]

        if lo > qhi + 1:
            q.append([lo, hi])
            continue

        q[-1][1] = max(qhi, hi)

    cannot = set()
    for lo, hi in q:
        for x in range(lo, hi+1):
            cannot.add(x)

    print(len(cannot - known))

def part2():
    
    input_str = read_input(day=DAY, test=TEST)
    lines = [list(map(int, re.findall(r'-?\d+', line))) for line in input_str.splitlines()]
    M = 20 if TEST else 4000000


    for Y in range(M+1):
        intervals = []
        for sx, sy, bx, by in lines:
            d = dist(sx, sy, bx, by)
            o = d - abs(sy - Y)

            if o < 0:
                continue

            lx = sx - o
            hx = sx + o
            intervals.append([lx, hx])

        intervals.sort()

        q = []
        for lo, hi in intervals:
            if not q:
                q.append([lo, hi])
                continue

            qlo, qhi = q[-1]

            if lo > qhi + 1:
                q.append([lo, hi])
                continue

            q[-1][1] = max(qhi, hi)
        
        x = 0
        for lo, hi in q:
            if x < lo:
                print(x * 4000000 + Y)
                exit(0)
            else:
                x = hi + 1
            if x > M:
                break


# part1()
part2()