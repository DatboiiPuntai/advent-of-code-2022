from utils import read_input
import operator
import math

DAY = 11
TEST = False

class Monkey:
    def __init__(self, items, op, value, div, true, false):
        self.items = items
        self.op = op 
        self.value = value
        self.div = div
        self.true = true
        self.false = false
        self.actions=0

def parse(input_str: str):
    monkes = []
    for m in input_str.split('\n\n'):
        _, a, b, c, d, e = m.split('\n')
        items = list(map(int, a.split(': ')[1].split(',')))
        op = b.split(' ')[-2]
        value = b.split(' ')[-1]
        div = int(c.split(' ')[-1])
        true = int(d.split(' ')[-1])
        false = int(e.split(' ')[-1])
        monkes.append(Monkey(items, op, value, div, true, false))
    return monkes


def part1(monkes):
    ROUNDS = 20
    for round in range(ROUNDS):
        for m in monkes:
            for item in m.items:
                num = item if m.value == 'old' else int(m.value)
                result = eval(f"{item} {m.op} {num}")
                # worry goes down
                item = result//3
                destination = m.false if item % m.div else m.true
                monkes[destination].items += [item]
                m.actions += 1
            m.items = []

    counts = sorted([m.actions for m in monkes])
    return counts[-1] * counts[-2]


def part2(monkes):
    ROUNDS = 10000
    product = math.prod([m.div for m in monkes])
    for round in range(ROUNDS):
        for m in monkes:
            for item in m.items:
                value = item if m.value == 'old' else int(m.value)
                result = eval(f"{item} {m.op} {value}")

                item = result % product
                destination = m.false if item % m.div else m.true
                monkes[destination].items += [item]
                m.actions += 1
            m.items = []

    counts = sorted([m.actions for m in monkes])
    return counts[-1] * counts[-2]


def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    data = parse(input_str)
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
