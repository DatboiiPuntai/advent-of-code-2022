from utils import read_input

DAY = 10
TEST = False

def parse(input_str: str):
    data = []
    for line in input_str.split('\n'):
        cmd = line.split()
        if len(cmd) > 1:
            data.append((cmd[0], int(cmd[1])))
        else:
            data.append((cmd[0], 0))
    return data


signalStrengths = []
cycle = 1
x = 1
def part1(data):
    global x
    print(f'Cycle: {cycle} x: {x}')
    for cmd, value in data:
        if cmd != 'addx':
            clockCPU()
        else:
            clockCPU()
            x += value
            clockCPU()
            
    
    return sum(signalStrengths)
            
def clockCPU():
    global signalStrengths, cycle, x
    cycle += 1
    if cycle in range(20, 221, 40):
        print(f'Cycle: {cycle} x: {x}')
        signalStrengths.append(x * cycle)
    else:
        print(f'Cycle: {cycle} x: {x}')


        
cycle = 1
x = 1
screen = [['.' for _ in range(40)] for _ in range(6)]
def part2(data):
    global x
    print(f'Cycle: {cycle} x: {x}')
    checkScreen()
    for cmd, value in data:
        if cmd != 'addx':
            clockCPU()
            checkScreen()
        else:
            clockCPU()
            checkScreen()
            x += value
            clockCPU()
            checkScreen()
    
    for i in screen:
        for j in i:
            print(j, end='')
        print()
    pass

def checkScreen():
    global cycle, x, screen
    
    row = (cycle-1)//40
    column = (cycle-1)%40
    print(f'{row=} {column=}')
    if (cycle-1)%40 in range(x-1, x+2):
        screen[row][column] = '#'
        print('Printed!')


def main():
    global cycle, x
    input_str = read_input(day=DAY, test=TEST)
    data = parse(input_str)
    # print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
