from utils import read_input
import json
from functools import cmp_to_key
from pprint import pprint

DAY = 13
TEST = False


def parse(input_str: str):
    pairs = [pair.split('\n') for pair in input_str.split('\n\n')]

    parsed = [list(map(json.loads, pair)) for pair in pairs]
    return parsed


def part1(pairs):
    counter = 0
    for i, pair in enumerate(pairs):
        left, right = pair
        if rightOrder(left, right) < 0:
            counter += i+1
    return counter


def rightOrder(left, right):
    for i in range(min(len(left), len(right))):
        if type(left[i]) == type(right[i]) == int:
            if left[i] == right[i]:
                continue
            return left[i] - right[i]
        ret = rightOrder(left[i] if type(left[i]) == list else [left[i]],
                         right[i] if type(right[i]) == list else [right[i]])

        if ret:
            return ret
    return len(left) - len(right)


def part2(pairs):
    items = [item for pair in pairs for item in pair]
    items += [[[2]], [[6]]]
    items = sorted(items, key=cmp_to_key(rightOrder))

    return (items.index([[2]]) + 1) * (items.index([[6]]) + 1)


def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
