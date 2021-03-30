#https://www.hackerrank.com/challenges/itertools-product/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a=map(int, raw_input().split(' '))
b=map(int, raw_input().split(' '))

l=map(str, list(product(a,b)))
print(' '.join(l))
