#https://www.hackerrank.com/challenges/capitalize/problem
s='chris alan'
def solve(s):
    arr = s.split(' ')
    for key, value in enumerate(arr):
        arr[key] = value.capitalize()
    
    print(' '.join(arr))

solve(s)
