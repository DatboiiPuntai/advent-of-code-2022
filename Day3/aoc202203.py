def main():
    with open(r'D:\Users\Pantai Suyasri\Documents\Programming\advent-of-code-2022\Day3\input.txt', 'r') as f:
        lines = f.read()

    rucksacks = lines.split('\n')

    # part 1
    rucksackCompartments = [(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:])
                            for rucksack in rucksacks]
    shared = []
    for rucksack in rucksackCompartments:
        shared.append(list(set(rucksack[0]) & set(rucksack[1]))[0])

    totalSum = 0
    for letter in shared:
        if letter.isupper():
            totalSum += ord(letter) - 38
        else:
            totalSum += ord(letter) - 96
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
