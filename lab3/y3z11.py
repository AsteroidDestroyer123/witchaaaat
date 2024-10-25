# найти значения n точек на промежутке [a,b] для функции y=cosx+xsinx
# найти найти для каждого экстремума значение x,y, вид экстремума
from math import cos,sin,pi
from random import uniform

n=int(input('введите колличество точек n'))
a=int(input('введите начало отрезка'))
b=int(input('введите конец отрезка'))
x1=[]
y1=[]
for i in range(n):
    q=uniform(a,b)
    x1.append(q)
    y1.append((cos(q)+q*sin(q)))
m=[]
for i in range(-10000,10000):
    if a<=(pi/2)+(i*pi)<=b:
        m.append(i)
x=[]
y=[]
for i in m:
    t=(pi/2)+(i*pi)
    x.append(t)
for i in m:
    t = (pi / 2) + (i * pi)
    y.append(cos(t)+((pi/2)+(i*pi))*sin(t))

print(x1)
print(y1)
print(x)
print(y)
t=[]
for i in y:
    if i<0:
        t.append(f'{i} - точка минимума')
    else:
        t.append(f'{i} - точка максимума')
print(t)