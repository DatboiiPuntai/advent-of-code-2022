from utils import read_input
from parse import *

DAY = 15
TEST = True


def parse(input_str: str):
    sensors = []
    beacons = []
    for line in input_str.split('\n'):
        sx = int(line.split()[2][2:-1])
        sy = int(line.split()[3][2:-1])
        bx = int(line.split()[8][2:-1])
        by = int(line.split()[9][2:])
        sensors.append((sx, sy))
        beacons.append((bx, by))

    return sensors, beacons


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# def interval_covering(start, stop, sorted_intervals, max_dim):
#     for covering_interval in sorted_intervals:
#         if stop >= max_dim:
#             return max_dim - (stop + 1)
#         if stop + 1 < covering_interval[0]:
#             return stop + 1
#         if (interval_right := covering_interval[1]) > stop:
#             stop = interval_right
#     return -1



def row_inspector(sensors, beacons, Y):
    
    dists = []
    for i in range(len(sensors)):
        dists.append(dist(sensors[i], beacons[i]))
    
    intervals = []
    for i, s in enumerate(sensors):
        dx = dists[i] - abs(s[1]-Y)
        if dx <=0:
            continue
        intervals.append((s[0] - dx, s[0] + dx))
    

    allowed_x = []
    for bx, by in beacons:
        if by == Y:
            allowed_x.append(bx)
    
    min_x = min(i[0] for i in intervals)
    max_x = max(i[1] for i in intervals)
    ans = 0
    for x in range(min_x, max_x+1):
        if x in allowed_x:
            continue
        for left, right in intervals:
            if left <= x <= right:
                ans += 1
                break
    return ans


def main():
    input_str = read_input(day=DAY, test=TEST)
    sensors, beacons = parse(input_str)
    print(row_inspector(sensors, beacons, 10))


if __name__ == "__main__":
    main()
