from utils import read_input

def main():
    lines = read_input(day=4)

    assignments = [line.split(',') for line in lines.split('\n')]

    for i in range(len(assignments)):
        assignments[i][0] = list(map(int, assignments[i][0].split('-')))
        assignments[i][1] = list(map(int, assignments[i][1].split('-')))

    # part 1
    count = 0
    for pair in assignments:
        set1 = set(range(pair[0][0], pair[0][1] + 1))
        set2 = set(range(pair[1][0], pair[1][1] + 1))
        if set1.issubset(set2) or set2.issubset(set1):
            count += 1
    print(count)

    # part 2
    count = 0
    for pair in assignments:
        set1 = set(range(pair[0][0], pair[0][1] + 1))
        set2 = set(range(pair[1][0], pair[1][1] + 1))
        if set1.intersection(set2):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
