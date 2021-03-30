#https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen
from collections import OrderedDict
def split(word): 
    return [char for char in word]

def merge_the_tools(string, k):
    db = int(len(string) / k)
    for i in range(db):
        print(''.join(list(OrderedDict.fromkeys(split(string[i * k:i * k + k])))))

merge_the_tools('123456789', 3)