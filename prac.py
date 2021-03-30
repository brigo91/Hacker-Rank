"""
class MyNumbers:
    def __iter__(self):
      print("__iter__")
      self.a = 1
      return self

    def __next__(self):
      print("__next__")
      x = self.a
      self.a += 1
      return x

    def __init__(self):
      print("__init__")

print("init")
myclass = MyNumbers()
print("iter")
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

myiter2 = iter(myclass)
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
"""
"""
def Counter(init = 0):
    def Count():
        nonlocal init
        init += 1
        return init
    return Count

myCounter = Counter()
myCounter()
myCounter()
myCounter()
myCounter()
myOtherCounter = Counter(100)
myOtherCounter()
myOtherCounter()
lof = myOtherCounter()
print(lof)
"""

class lof():
    def __del__(self):
        print("lof")

    def loff(self):
        print("asdasdads")

a = lof()
b = a
del(b)
b.loff()
del(b)