arr = [2,3,6,6,5]
maxim = max(arr)
try:
    while True:
        arr.remove(maxim)
except ValueError:
    print(max(arr))