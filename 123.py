
'''
2 уровень 2 задание
найти наибольшее значение n для которого сумма p = 1*4*7*...*n не превышает L=30000
'''

L=1
n=1
while L <= 30000:
    L=1
    for i in range(1,n+1,3):
        L*=i
    n+=3
else:
    print(n-6)
