#https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
a=raw_input()
lenhgth=int(a[-1])
a=''.join(sorted(a[:-2:]))
a=list(permutations(a, lenhgth))
a=map(''.join, a)
for i in a:
    print(i)