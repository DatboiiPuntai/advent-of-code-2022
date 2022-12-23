from utils import read_input

DAY = 23
TEST = False

input_str = read_input(day=DAY, test=TEST)

elves = set()
for r, line in enumerate(input_str.splitlines()):
    for c, item in enumerate(line):
        if item == '#':
            elves.add(c+r * 1j)

scanmap = {
    -1j: [-1j-1, -1j, -1j+1],
    1j: [1j-1, 1j, 1j+1],
    -1: [-1-1j, -1, -1+1j],
    1: [1-1j, 1, 1+1j],
}
#        N    S   W   E
moves = [-1j, 1j, -1, 1]
N = [-1-1j, -1j, 1-1j, 1, 1+1j, 1j, -1+1j, -1]

last = elves.copy()
count = 1
while True:
    once = set()
    twice = set()
    for elf in elves:
        # check if isolated
        if all(elf + x not in elves for x in N):
            continue
        for move in moves:
            # check if direction is a valid move
            if all(elf + x not in elves for x in scanmap[move]):
                prop = elf + move
                if prop in twice:
                    pass
                elif prop in once:
                    twice.add(prop)
                else:
                    once.add(prop)
                break
    
    # commit moves
    ec = elves.copy()
    for elf in ec:
        if all(elf + x not in ec for x in N):
            continue
        for move in moves:
            if all(elf + x not in ec for x in scanmap[move]):
                prop = elf + move
                if prop not in twice:
                    elves.remove(elf)
                    elves.add(prop)
                break

    moves.append(moves.pop(0))

    if last == elves:
        break
    last = elves.copy()
    count += 1

# minx = min(n.real for n in elves)
# maxx = max(n.real for n in elves)
# miny = min(n.imag for n in elves)
# maxy = max(n.imag for n in elves)

# print((maxx-minx+1) * (maxy-miny+1) - len(elves))
print(count)