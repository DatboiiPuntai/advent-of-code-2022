from utils import read_input
import z3

DAY = 21
TEST = False


input_str = read_input(day=DAY, test=TEST)

monkes = {}
for line in input_str.splitlines():
    x = line.split(': ')
    name = x[0]
    if len(x[1].split()) > 1:
        monkes[name] = x[1].split()
    else:
        monkes[name] = int(x[1])


def solve1(root):
    if type(monkes[root]) is int:
        return monkes[root]
    else:
        return eval(f'{solve1(monkes[root][0])} {monkes[root][1]} {solve1(monkes[root][2])}')

print(solve1('root'))


# part 2
solver = z3.Optimize()

monkeys = {}

for monkey in input_str.splitlines():
    name, op = monkey.split(": ")

    if name == "humn":
        continue
    elif name == "root":
        m1, _, m2 = op.split(" ")
        m1 = monkeys.setdefault(m1, z3.Int(m1))
        m2 = monkeys.setdefault(m2, z3.Int(m2))
        solver.add(m1 == m2)
        continue

    match (op.split(" ")):
        case [n]:
            m = monkeys.setdefault(name, z3.Int(name))
            solver.add(m == n)
        case [m1, "+", m2]:
            m = monkeys.setdefault(name, z3.Int(name))
            m1 = monkeys.setdefault(m1, z3.Int(m1))
            m2 = monkeys.setdefault(m2, z3.Int(m2))
            solver.add(m == (m1 + m2))
        case [m1, "-", m2]:
            m = monkeys.setdefault(name, z3.Int(name))
            m1 = monkeys.setdefault(m1, z3.Int(m1))
            m2 = monkeys.setdefault(m2, z3.Int(m2))
            solver.add(m == (m1 - m2))
        case [m1, "*", m2]:
            m = monkeys.setdefault(name, z3.Int(name))
            m1 = monkeys.setdefault(m1, z3.Int(m1))
            m2 = monkeys.setdefault(m2, z3.Int(m2))
            solver.add(m == (m1 * m2))
        case [m1, "/", m2]:
            m = monkeys.setdefault(name, z3.Int(name))
            m1 = monkeys.setdefault(m1, z3.Int(m1))
            m2 = monkeys.setdefault(m2, z3.Int(m2))
            solver.add(m2 != 0)
            solver.add(m == (m1 / m2))

if solver.check() != z3.sat:
    raise Exception

humn = monkeys["humn"]
model = solver.model()
print(model[humn].as_long())