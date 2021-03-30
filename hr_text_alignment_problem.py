#https://www.hackerrank.com/challenges/text-alignment/problem
#https://www.hackerrank.com/challenges/text-wrap/problem

c = 'H'
thickness = 35

#Top Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))