#https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
import sys

for i in range(int(raw_input())):
    n = int(raw_input())
    cubes = deque(map(int, raw_input().split()))
    prev = sys.maxsize
    for j in range(n):
        is_left = True
        end = cubes[0]
        if cubes[0] < cubes[-1]:
            end = cubes[-1]
            is_left = False

        if end <= prev and is_left:
            prev = cubes.popleft()
        elif end <= prev and not is_left:
            prev = cubes.pop()
        else:
            break

    if len(cubes):
        print("No")
    else:
        print("Yes")