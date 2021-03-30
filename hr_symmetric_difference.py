#https://www.hackerrank.com/challenges/symmetric-difference/problem
raw_input()
M=set(map(int, raw_input().split()))
raw_input()
N=set(map(int, raw_input().split()))

for i in sorted((M.union(N)).difference((M.intersection(N)))):
    print(i)
