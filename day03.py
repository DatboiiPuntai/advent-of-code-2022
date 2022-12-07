from utils import read_input

def main():
    lines = read_input(day=3)

    rucksacks = lines.split('\n')

    # part 1
    totalSum = 0
    rucksackCompartments = [(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])
                            for rucksack in rucksacks]
    for rucksack in rucksackCompartments:
        shared = list(set(rucksack[0]) & set(rucksack[1]))[0]
        if shared.isupper():
            totalSum += ord(shared) - 38
        else:
            totalSum += ord(shared) - 96
        
    print(totalSum)

    # part 2
    totalSum = 0
    groups = [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]
    for group in groups:
        shared = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        if shared.isupper():
            totalSum += ord(shared) - 38
        else:
            totalSum += ord(shared) - 96
    print(totalSum)
    


if __name__ == '__main__':
    main()
