from utils import read_input
from collections import defaultdict
from math import inf
from operator import itemgetter
from itertools import combinations, product

DAY = 16
TEST = True

def floyd_warshall(g):
	distance = defaultdict(lambda: defaultdict(lambda: inf))

	for a, bs in g.items():
		distance[a][a] = 0

		for b in bs:
			distance[a][b] = 1
			distance[b][b] = 0

	for a, b, c in product(g, g, g):
		bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

		if ba + ac < bc:
			distance[b][c] = ba + ac

	return distance

def score(rates, valves):
	s = 0
	for v, t in valves.items():
		s += rates[v] * t
	return s
    
def choices(distance, rates, valves, time=30, cur='AA', chosen={}):
	for nxt in valves:
		new_time = time - distance[cur][nxt] - 1
		if new_time < 2:
			continue

		new_chosen = chosen | {nxt: new_time}
		yield from choices(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

	yield chosen

def parse(input_str: str):
    data = []
    for line in input_str.split('\n'):
        name = line.split()[1]
        rate = int(line.split()[4][5:-1])
        tunnels = line.replace('valves', 'valve').split(
            'valve ')[1].split(', ')
        data.append((name, rate, tunnels))

    return data


def part1(data):

    pass


def part2(data):
    pass


def main():
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
