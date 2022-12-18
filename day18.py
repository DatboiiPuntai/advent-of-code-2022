from utils import read_input


DAY = 18
TEST = False


input_str = read_input(day=DAY, test=TEST)

cubes = {tuple(map(int,line.split(','))) for line in input_str.split('\n')}
def sides(x,y,z):
	return {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

print(sum((s not in cubes) for c in cubes for s in sides(*c)))

seen = set()
todo = [(-1,-1,-1)]

while todo:
    here = todo.pop()
    todo += [s for s in (sides(*here) - cubes - seen) if all(-10<c<30 for c in s)]
    seen |= {here}

print(sum((s in seen) for c in cubes for s in sides(*c)))