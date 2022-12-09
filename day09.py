from utils import read_input
import math
DAY = 9
TEST = False
ROPE_LENGTH = 2


moveDict = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def parse(input_str: str):
    data = [(line.split()[0], int(line.split()[1]))
            for line in input_str.split('\n')]
    return data


def touching(x1, y1, x2, y2):
    return abs(x1-x2) <= 1 and abs(y1-y2) <= 1


def move(dx, dy, snake):
    snake[0][0] += dx
    snake[0][1] += dy

    for i in range(1, ROPE_LENGTH):
        hx, hy = snake[i-1]
        tx, ty = snake[i]

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx-tx) / abs(hx-tx)
            sign_y = 0 if hy == ty else (hy-ty) / abs(hy-ty)
            tx += sign_x
            ty += sign_y
        snake[i] = [tx, ty]
    return snake


def part1(data):
    # change ROPE_LENGTH
    pass


def part2(data):
    snake = [[0, 0] for _ in range(ROPE_LENGTH)]

    tail_visited = set()
    tail_visited.add(tuple(snake[-1]))

    for dir, amount in data:
        dx, dy = moveDict[dir]
        for _ in range(amount):
            snake = move(dx, dy, snake)
            tail_visited.add(tuple(snake[-1]))
    return (len(tail_visited))


def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
