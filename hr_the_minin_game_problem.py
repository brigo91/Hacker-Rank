#https://www.hackerrank.com/challenges/the-minion-game/problem

def minion(s):
    kevin_score = 0
    stuart_score = 0
    for i in s:
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            kevin_score += len(s) - i
        else:
            stuart_score += len(s) - i
    
    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score < stuart_score :
        print('Stuart {}'.format(stuart_score))
    else:
        print('Kevin {}'.format(kevin_score))


