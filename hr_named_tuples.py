#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(raw_input())
Students = namedtuple('Students', ' '.join(raw_input().split()))

sum = 0

for i in range(N):
    stud = Students(*(raw_input().split()))
    sum += int(stud.MARKS)

print(float(sum)/N)