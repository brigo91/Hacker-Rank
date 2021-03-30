def wrapper(f):
    def fun(l):
        li = []
        for tel in l:
            if len(tel) == 13:
                tel = tel[:3] + ' ' + tel[3:8] + ' ' + tel[8:]
            elif len(tel) == 12:
                tel = '+' + tel[:2] + ' ' + tel[2:7] + ' ' +tel[7:]
            elif len(tel) == 11:
                tel = '+91' + ' ' + tel[1:6] + ' ' + tel[6:]
            else:
                tel = '+91' + ' ' + tel[:5] + ' ' + tel[5:]
            li.append(tel)
        f(li)
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l) 