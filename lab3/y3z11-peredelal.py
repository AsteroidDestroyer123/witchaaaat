# найти значения n точек на промежутке [a,b] для функции y=cosx+xsinx
# найти найти для каждого экстремума значение x,y, вид экстремума
from math import cos,sin,pi
from random import uniform
import numpy as np

n=int(input('введите колличество точек n'))
a=float(input('введите начало отрезка'))
b=float(input('введите конец отрезка'))
x1=[]
y1=[]
for g in range(n):
    q=uniform(a,b)
    x1.append(q)
    y1.append((cos(q)+q*sin(q)))
m=[]
for i in np.arange(a,b+1):
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
print('точки на промежутке')
for i in range(len(x1)):
    print(f'x:{x1[i]}')
    print(f'y:{y1[i]}')
print('координаты экстремумов')
for i in range(len(x)):
    print(f'x:{x[i]}')
    print(f'y:{y[i]}')
if a<0<b:
    print('x:0')
    print('y:1')
t=[]
for i in y:
    if i<0:
        t.append(f'{i} - точка минимума')
    else:
        t.append(f'{i} - точка максимума')
print('классификация экстремумов')
t.append('0 - точка минимума')
print(t)
