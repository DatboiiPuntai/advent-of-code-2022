from utils import read_input

DAY = 17
TEST = False

height = 80
width = 7
grid = [['.' for _ in range(width)] for _ in range(height)]
highest_rock = -1

rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1+1j, 2+1j, 1+2j],
    [0, 1, 2, 2+1j, 2+2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1+1j],
]

jets = [1 if x == '>' else -1 for x in read_input(day=DAY, test=TEST)]
solid = {x - 1j for x in range (7)}
height = 0

rock_count = 0
rock_index = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

a = []

while rock_count < 5000:
    for jet in jets:
        # perform side movement and check collision
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock = moved
        
        # vertical movement
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rock_count += 1
            old = height
            height = max(x.imag for x in solid) + 1
            a.append(int(height-old))
            if rock_count >= 5000:
                break
            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
        else:
            rock = moved

print(int(height))
print(','.join(map(str, a)))

# random manual stuff

# input = '4,2,1,2,3,2,2,0,0,3,1,1,1,3,3,0,0,1,2,2,1,1,1,3,3,0,0,1,3,0,3,0,0,0,3,4,2,1,2,1,4,2,1,3,2,1,2,1,0,3,0,2,1,3,3,0,0,0,2,2,2,2,1,3,0,3,0,0,3,0,3,0,0,2,1,2,0,1,2,1,2,2,1,3,2,2,2,1,3,2,1,0,1,1,2,1,0,1,3,3,0,0,1,3,2,2,2,1,3,2,2,2,1,3,3,2,2,1,3,2,2,0,0,3,3,2,0,0,2,0,3,0,1,3,3,2,2,1,3,3,4,0,0,0,3,2,0,1,3,3,2,0,1,3,2,0,0,1,1,2,2,0,1,3,3,2,2,1,3,3,0,0,1,3,0,0,2,1,3,0,4,0,0,1,3,2,0,1,3,3,0,0,1,2,3,0,1,1,2,1,3,0,0,3,2,0,2,1,2,1,3,2,0,0,3,0,2,1,3,2,2,0,1,1,2,2,0,1,2,3,0,0,0,3,0,2,2,1,3,2,2,0,1,3,2,0,0,1,3,3,4,0,1,3,3,2,2,1,1,2,1,0,0,2,1,3,0,0,2,3,2,0,1,2,1,2,0,0,3,2,4,0,1,2,2,0,2,1,3,0,2,0,1,3,0,2,2,1,2,3,0,1,0,3,3,4,0,1,3,3,4,0,1,3,3,0,0,1,3,0,3,2,1,0,3,1,1,1,3,2,2,0,0,2,2,0,2,1,3,3,0,0,1,2,3,2,2,1,2,3,0,2,1,3,2,0,0,1,2,1,2,0,0,2,2,2,2,1,3,3,2,2,0,0,3,2,2,1,3,3,4,0,1,3,0,4,0,1,2,3,0,2,1,3,2,2,0,1,2,2,1,1,1,3,0,4,0,1,3,3,2,0,0,0,1,0,2,1,3,3,0,2,1,3,0,2,0,1,2,2,0,2,0,2,3,0,0,1,3,3,0,0,1,3,0,2,0,1,3,2,2,0,0,2,2,0,0,1,3,3,0,2,1,0,3,2,2,1,3,2,1,0,1,2,3,4,0,1,2,1,1,0,1,2,3,0,0,1,3,3,0,2,0,3,3,0,0,1,3,3,0,0,1,2,3,0,2,0,2,3,2,0,1,3,3,2,0,1,3,3,2,0,0,2,2,2,2,1,3,3,0,0,1,3,2,0,1,1,3,0,3,0,1,3,2,2,0,1,3,2,2,2,1,2,2,2,0,1,2,3,0,0,1,3,3,2,2,1,3,2,2,0,1,2,3,0,0,1,2,3,2,2,1,3,3,2,0,1,3,0,3,2,0,0,2,0,0,1,3,3,0,0,0,2,2,0,0,1,3,2,1,0,1,3,2,4,0,0,0,3,0,2,1,0,3,2,2,1,3,3,0,0,1,2,2,2,2,0,0,3,4,2,1,3,3,0,0,1,2,3,0,2,1,0,2,4,0,1,3,3,2,0,1,3,3,2,2,1,2,1,3,0,0,1,2,2,2,0,0,3,1,2,1,3,3,2,2,1,2,1,2,0,1,3,2,4,2,0,0,3,0,2,1,3,2,2,2,0,0,3,2,2,1,3,3,2,0,1,3,0,1,1,0,3,2,2,0,1,2,2,2,0,1,0,3,1,2,1,3,0,2,0,1,3,3,2,0,1,3,3,0,0,1,3,0,3,0,1,2,2,1,1,1,2,3,4,0,1,3,3,2,0,1,3,3,2,2,1,3,3,0,0,0,1,1,2,2,1,2,2,2,0,1,3,0,2,0,1,3,3,0,0,1,2,1,2,2,0,0,3,1,2,1,3,3,4,2,0,3,2,4,0,1,3,0,4,2,1,3,3,2,0,1,3,3,0,2,1,2,2,2,0,1,2,2,2,0,1,3,0,3,0,1,3,2,1,1,1,2,3,0,2,1,2,1,2,2,1,3,3,4,0,1,3,0,3,0,0,3,0,2,0,1,2,3,4,2,1,3,0,0,0,1,3,0,4,0,0,2,3,2,2,1,2,1,0,0,1,3,2,2,0,1,3,2,2,2,1,3,3,4,0,1,3,3,2,2,0,0,3,2,2,1,3,2,2,0,0,3,0,3,2,1,2,3,4,2,1,3,3,4,0,1,2,1,2,0,0,3,0,4,2,1,0,3,0,0,1,3,2,4,0,1,3,3,2,2,1,2,1,2,0,1,3,3,2,2,1,3,2,2,2,0,0,3,1,0,0,3,2,0,0,1,3,3,2,0,0,3,2,1,2,0,1,3,2,0,1,3,3,0,0,1,3,3,0,0,1,3,3,0,0,1,3,3,4,0,1,2,1,3,2,1,2,1,2,0,1,3,2,4,0,1,3,2,0,0,1,3,2,0,2,0,2,3,0,0,1,1,2,2,2,1,3,3,2,0,0,3,2,2,0,1,3,2,2,0,1,2,1,2,0,1,3,3,0,0,1,3,3,0,0,1,3,2,2,2,0,0,0,4,0,1,2,3,4,0,1,3,3,2,0,1,3,2,2,0,1,3,2,1,0,1,2,2,2,0,0,2,0,3,0,0,2,3,2,0,1,3,2,1,1,1,3,3,4,0,1,2,3,2,0,0,0,2,0,0,1,3,2,0,0,1,0,3,4,0,1,3,0,0,0,0,3,0,2,0,0,3,0,3,2,0,0,3,4,0,1,3,0,0,1,1,3,2,2,2,0,0,3,2,2,0,2,2,1,2,1,3,2,4,0,0,0,1,0,2,1,3,2,0,0,0,3,0,2,0,1,3,3,0,0,1,2,1,2,0,0,2,3,0,0,1,3,3,4,0,1,2,1,2,0,0,2,0,3,0,0,1,2,4,0,1,3,0,3,0,1,3,3,2,2,1,3,3,2,2,1,2,1,2,2,1,2,3,0,2,1,3,2,0,0,1,2,2,0,2,1,3,0,2,2,1,2,2,0,2,1,3,3,2,0,1,3,2,2,0,1,3,2,2,2,1,2,3,0,0,0,2,1,3,0,1,3,3,2,2,1,3,2,2,2,1,3,3,0,2,1,3,0,2,0,1,1,2,4,0,1,3,0,0,2,0,3,2,0,0,1,3,3,0,0,1,3,3,0,0,1,2,1,3,0,1,3,0,3,0,1,3,3,2,0,1,2,3,0,2,1,3,2,2,0,1,3,3,2,0,1,3,3,0,0,1,3,3,2,0,1,3,0,4,0,0,3,2,2,2,1,3,3,4,2,1,3,0,0,0,1,3,3,0,0,1,2,3,0,0,1,3,3,0,2,1,3,3,0,0,1,3,0,3,0,1,3,3,4,0,1,3,2,2,0,0,1,3,4,0,0,2,2,4,0,1,2,2,0,0,1,3,3,0,0,0,2,3,4,0,0,0,3,4,0,1,3,2,2,2,1,3,2,2,0,1,3,2,2,0,1,3,3,0,0,1,3,0,2,0,1,3,3,0,0,1,3,0,1,1,0,3,0,2,0,1,2,2,2,0,1,2,2,2,0,1,0,2,2,0,1,3,3,0,0,1,3,3,0,0,0,2,3,2,0,1,2,2,2,2,1,3,2,1,2,1,2,3,4,2,1,3,3,2,0,1,0,3,1,0,0,3,3,4,0,0,0,3,0,0,1,3,2,4,2,1,3,2,1,1,1,3,3,4,0,1,3,2,1,0,1,3,3,2,0,1,3,2,1,1,1,3,2,2,0,1,3,3,2,0,1,3,2,2,0,1,2,1,3,0,0,2,3,0,0,1,3,3,0,0,1,3,2,4,0,0,0,1,2,2,1,2,3,4,0,1,3,3,0,2,1,3,3,2,0,1,2,2,4,2,0,2,3,4,0,1,3,2,2,2,0,0,3,1,0,1,2,2,2,0,1,3,3,2,2,1,2,2'
# first = '1,2,3,4,0,1,3,3,2,0,1,3,3,0,0,1,3,3,2,0,1,3,2,4,0,0,0,3,2,0,1,3,0,2,2,1,2,2,2,0,1,3,3,2,0,0,2,2,4,0,1,3,3,4,0,1,2,1,3,0,1,3,3,2,0,1,3,2,2,2,1,3,3,0,2,1,2,3,0,0,1,3,2,1,1,1,3,3,0,0,0,2,2,2,0,1,3,2,2,0,0,3,0,1,0,0,2,2,4,0,0,0,3,4,2,1,2,3,0,1,1,3,2,4,2,1,3,2,1,0,0,3,2,2,0,1,3,3,0,0,1,2,3,0,0,1,3,0,3,0,0,2,0,1,2,1,3,2,4,0,0,3,2,2,0,1,2,1,3,0,0,2,3,0,0,1,3,3,2,2,1,3,3,0,0,0,2,2,1,0,1,3,2,1,1,1,3,2,0,0,0,3,3,0,0,0,2,3,0,1,0,3,0,2,0,1,3,3,2,2,1,3,3,0,0,1,0,3'
# # input = '1,2,1,2,0,1,2,1,2,0,1,3,2,0,0,1,3,3,4,0,1,2,3,0,1,1,3,2,2,0,0,2,3,4,0,1,2,1,2,0,1,2,1,2,0,1,3,2,0,0,1,3,3,4,0,1,2,3,0,1,1,3,2,2,0,0,2,3,4,0,1,2,1,2,0,1,2,1,2,0,1,3,2,0,0,1,3,3,4,0,1,2,3,0,1,1,3,2,2,0,0,2,3,4,0'
# # first = '1,3,2,1,2,1,3,2,2,0,1,3,2,0,2,1,3,3,4,0,1,2,3,0,1,1,3,2,2,0,0,2,3,4,0'
# nums = [int(x) for x in input.split(',')]
# firstnums = [int(x) for x in first.split(',')]

# firstLength = len(firstnums)
# firstSum = sum(firstnums)

# patternLength = len(nums)
# patternSum = sum(nums)

# numPattern = (1000000000000 - firstLength) // patternLength
# overhang = (1000000000000 - firstLength) % patternLength
# print((numPattern * patternSum) + firstSum + sum(nums[:overhang]))