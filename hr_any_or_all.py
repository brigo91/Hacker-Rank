#https://www.hackerrank.com/challenges/any-or-all/problem
N = raw_input()
l = raw_input().split()
print(all(map(lambda x: x > 0, map(int,l))) and any(map(lambda x: x == x[::-1], l)))