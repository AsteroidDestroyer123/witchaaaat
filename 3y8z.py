'''
3 уровень 8 задание
сумаа от i==0 до бесконечности ((2*x)**i)/(factorial(i))    
y=e**(2*x)
x в диапазоне от 0.1 до 1 с шагом 0.05
'''
from math import factorial


x=0.1
while x<1:
    y=(2.7182)**(2*x)
    s=0
    i=0
    e=1
    while abs(e)>0.0001:
        e=((2*x)**i)/(factorial(i))
        s+=e
        i+=1
    print(s,y)
    x+=0.05
