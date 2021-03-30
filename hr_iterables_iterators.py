#https://www.hackerrank.com/challenges/iterables-and-iterators/problem
import itertools
raw_input()
l = raw_input().split()
k =int(raw_input())

length = 0
positive = 0
for i in itertools.combinations(l, k):
    if 'a' in i:
        positive += 1 
    length += 1

print(float(positive)/length)
