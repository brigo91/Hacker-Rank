#https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
d = deque()
commands = {
    'append': d.append,
    'pop': d.pop,
    'popleft': d.popleft,
    'appendleft': d.appendleft,
}

for i in range(int(raw_input())):
    com = raw_input().split()
    if len(com) == 1:
        commands[com[0]]()
    else:
        commands[com[0]](com[1])

print(" ".join(d))