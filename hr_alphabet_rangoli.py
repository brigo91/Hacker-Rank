#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string
abc = string.ascii_lowercase


n = 5

#midle
# print(abc[n - 1:0:-1] + abc[:n])

def split(word): 
    return [char for char in word]

down = []

for i in range(n, 1, -1):
    temp = abc[n - 1:n - i:-1]
    rev = temp[::-1]
    striped = '-'.join(split((temp + rev[1::])))
    down.append(striped.center(2*(2*n-1) -1, '-'))

up = down[::-1]


for element in up:
    print(element)

print('-'.join(split(abc[n - 1:0:-1] + abc[:n])))

for element in down:
    print(element)
