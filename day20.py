from utils import read_input
from collections import deque

DAY = 20
TEST = False


input_str = read_input(day=DAY, test=TEST)


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

r = []
input_str = read_input(day=DAY, test=TEST)
for l in input_str.splitlines():
    r.append(Node(int(l)))

for a, b in zip(r,r[1:]):
    a.next = b
    b.prev = a
r[-1].next = r[0]
r[0].prev = r[-1]

for x in r:
    # split the circular thing
    x.prev.next = x.next
    x.next.prev = x.prev
    a,b = x.prev, x.next

    for _ in range(x.value % (len(r) - 1)):
        a=a.next
        b=b.next
    a.next = x
    x.prev = a
    b.prev = x
    x.next = b

total = 0
for x in r:
    if x.value == 0:
        y = x
        for _ in range(3):
            for _ in range(1000):
                y = y.next
            total += y.value
        print(total)


# part 2 
r = []
for l in input_str.splitlines():
    n = 811589153 * int(l)
    r.append(Node(n))

for a, b in zip(r,r[1:]):
    a.next = b
    b.prev = a
r[-1].next = r[0]
r[0].prev = r[-1]


for _ in range(10):
    for x in r:
        x.prev.next = x.next
        x.next.prev = x.prev
        a,b = x.prev, x.next

        for _ in range(x.value % (len(r) - 1)):
            a=a.next
            b=b.next
        a.next = x
        x.prev = a
        b.prev = x
        x.next = b

total = 0
for x in r:
    if x.value == 0:
        y = x
        for _ in range(3):
            for _ in range(1000):
                y = y.next
            total += y.value
        print(total)
