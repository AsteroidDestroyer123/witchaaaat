'''
3 уровень 2 задание
сумаа от i==1 до бесконечности ((x**i)*(sin((i*3.14)/4)))  
y=(x*sin(3.14/4))/(1-2*x*cos(3.14/4)+x**2)
x в диапазоне от 0.1 до 0.8 с шагом 0.1
'''
from math import cos, sin


x=0.1
while x<0.8:
    y=(x*sin(3.14/4))/(1-2*x*cos(3.14/4)+x**2)
    s=0
    i=1
    e=1
    while abs(e)>0.0001:
        e=((x**i)*(sin((i*3.14)/4)))
        s+=e
        i+=1
    print(s,y)
    x+=0.1
