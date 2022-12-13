from utils import read_input
import math
DAY = 8
TEST = False


def parse(input_str: str):
    trees = [[int(n) for n in list(line)] for line in input_str.split()]
    return trees


def part1(data):
    visible = set()
    # top to bottom
    for i in range(len(data)):
        max = -1
        for j in range(len(data)):
            if data[j][i] > max:
                visible.add((j, i))
                max = data[j][i]

    # bottom to top
    for i in range(len(data))[::-1]:
        max = -1
        for j in range(len(data))[::-1]:
            if data[j][i] > max:
                visible.add((j, i))
                max = data[j][i]
    # left to right
    for i in range(len(data)):
        max = -1
        for j in range(len(data)):
            if data[i][j] > max:
                visible.add((i, j))
                max = data[i][j]
    # right to left
    for i in range(len(data))[::-1]:
        max = -1
        for j in range(len(data))[::-1]:
            if data[i][j] > max:
                visible.add((i, j))
                max = data[i][j]
    return len(visible)


def part2(data):
    scenicScores = []
    for i in range(len(data))[1:-1]:
        for j in range(len(data))[1:-1]:
            viewingAngles = []
            # looking up
            counter = 0
            for k in range(1,i+1):
                if data[i-k][j] >= data[i][j]:
                    counter += 1
                    break
                else:
                    counter += 1
            viewingAngles.append(counter)
            # looking down
            counter = 0
            for k in range(1,len(data)-i):
                if data[i+k][j] >= data[i][j]:
                    counter += 1
                    break
                else:
                    counter += 1
            viewingAngles.append(counter)
            # looking left
            counter = 0
            for k in range(1,len(data)-j):
                if data[i][j+k] >= data[i][j]:
                    counter += 1
                    break
                else:
                    counter += 1
            viewingAngles.append(counter)
            # looking right
            counter = 0
            for k in range(1,j+1):
                if data[i][j-k] >= data[i][j]:
                    counter += 1
                    break
                else:
                    counter += 1
            viewingAngles.append(counter)
            scenicScores.append(math.prod(viewingAngles))
    return max(scenicScores)

def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
