from utils import read_input

def main():
    lines = read_input(day=1)
    elves = lines.split('\n\n')

    calories = []
    for elf in elves:
        calorieSum = sum(map(int, elf.split()))
        calories.append(calorieSum)

    # part 1
    print(max(calories))
    # part 2
    print(sum(sorted(calories, reverse=True)[:3]))


if __name__ == '__main__':
    main()
