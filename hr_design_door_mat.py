#https://www.hackerrank.com/challenges/designer-door-mat/problem

N = 15
M = 45

#print((3*'.|.').center(27, '-'))

for i in range(int((N+1)/2) - 1):
    print(( (2*i + 1)*'.|.').center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(int((N+1)/2) - 2, -1, -1):
    print(( (2*i + 1)*'.|.').center(M, '-'))