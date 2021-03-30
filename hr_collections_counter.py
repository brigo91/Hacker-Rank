#https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = raw_input()
shoes = map(int, raw_input().split())
N = int(raw_input())
shoes = Counter(shoes)
money = 0
for i in range(N):
    p = map(int, raw_input().split())
    if shoes[p[0]]:
        money += p[1]
        shoes[p[0]] -= 1
    
print(money)