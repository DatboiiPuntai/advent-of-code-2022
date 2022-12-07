from utils import read_input

WIDTH = 9


def main():
    lines = read_input(day=5)
    diagram, instructions = lines.split('\n\n')

    stacks = [[] for _ in range(WIDTH)]
    diagramLines = diagram.split('\n')
    for line in diagramLines:
        for i in range(WIDTH):
            if line[i*4+1] != ' ' and line[i*4+1].isalpha:
                stacks[i].append(line[i*4+1])
    print(stacks)



    for line in instructions.split('\n'):
        numMoved = int(line.split(' ')[1])
        fromStack = int(line.split(' ')[3]) - 1
        toStack = int(line.split(' ')[-1]) - 1
        # # part 1
        # for i in range(numMoved):
        #     crate = stacks[fromStack].pop(0)
        #     stacks[toStack].insert(0, crate)

        # part 2
        crate = stacks[fromStack][:numMoved]
        for item in crate:
            stacks[fromStack].remove(item)
        stacks[toStack] = crate + stacks[toStack]
        print(stacks)

    for stack in stacks:
        print(stack[0], end='')


if __name__ == '__main__':
    main()
