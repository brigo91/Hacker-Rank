#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(raw_input())
summa = OrderedDict()
solditems = [' '.join(raw_input().split()) for i in range(N)]
solditems = [(' '.join(i.split()[:-1]), int(i.split()[-1])) for i in solditems]

for i in solditems:
    if not(i[0] in summa):
        summa[i[0]] = 0
    
    summa[i[0]] += i[1]

for i, k in summa.items():
    print(str(i) + ' ' + str(k))