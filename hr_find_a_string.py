#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    list_of_indexes = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(list_of_indexes)
