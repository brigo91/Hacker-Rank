if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_tuple = tuple(integer_list)
    print(hash(int_tuple))