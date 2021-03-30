#https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,raw_input().split())
theArray = map(int,raw_input().split())
A = set(map(int,raw_input().split()))
B = set(map(int,raw_input().split()))

happiness = 0
for i in theArray:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
