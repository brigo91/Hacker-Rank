#https://www.hackerrank.com/challenges/zipped/problem
N, X = map(int, raw_input().split())
l = []
for i in range(X):
    l.append(map(float, raw_input().split()))

zipped = zip(*l)
for i in zipped:
    print(sum(i)/len(i))
   