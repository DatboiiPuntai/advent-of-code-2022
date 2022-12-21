from utils import read_input
import sympy

DAY = 21
TEST = False


input_str = read_input(day=DAY, test=TEST)

monkes = {}
for line in input_str.splitlines():
    name, expr = line.split(': ')
    if expr.isdigit():
        monkes[name] = int(expr)
    else:
        monkes[name] = expr.split()
        

def solve1(root):
    if type(monkes[root]) is int:
        return monkes[root]
    else:
        return eval(f'{solve1(monkes[root][0])} {monkes[root][1]} {solve1(monkes[root][2])}')

print(solve1('root'))


ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

# part 2
del monkes
monkes = {'humn': sympy.Symbol('x')}

x = [line.strip() for line in input_str.splitlines()]
for a in x:
    name, expr = a.split(': ')
    if name in monkes: continue
    if expr.isdigit():
        monkes[name] = int(expr)
    else:
        left, op, right = expr.split()
        if left in monkes and right in monkes:
            if name == 'root':
                print(round(sympy.solve(monkes[left] - monkes[right])[0]))
                break
            monkes[name] = ops[op](monkes[left], monkes[right])
        else:
            x.append(a)