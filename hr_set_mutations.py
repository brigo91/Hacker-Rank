#https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
S = set(map(int, raw_input().split()))
N = int(raw_input())
for i in range(N):
    cmd = raw_input().split()[0]
    cmdSet = set(map(int, raw_input().split()))
    getattr(S, cmd)(cmdSet)

print(sum(S))