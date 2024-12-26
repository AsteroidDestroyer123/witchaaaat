#Посчитать суммы 
#1) S=1+(сумма от 1 до бесконечности)cos(x*i)/factorial(i), (e ** (cos(x))) * cos(sin(x))
#2) S=(сумма от 1 до бесконечности)((-1)**(i))*(cos(i*x))/(i**2), (x**2-((pi**2)/(3)))/4
from math import sin, pi, e, factorial,cos
import numpy as np

def z1(x,i):
    return(cos(x*i)/factorial(i))
def z11(x):
    return (e ** (cos(x))) * cos(sin(x))
def z2(x,i):
    return ((-1)**(i))*(cos(i*x))/(i**2)
def z22(x):
    return (x**2-((pi**2)/(3)))/4
def f1(for1,for2,a, b, h,p):
    results1 = []
    results2 = []
    for x in np.arange(a, b, h):
        delta2 = 0
        delta1 = for2(x)
        c = 0
        i = 1
        while abs(for1(x,i))>0.0000001: 
            delta2=for1(x,i)
            c += delta2
            i += 1
        print(c+p,delta1)
        
    
print('значения 1 функции')
f1(z1,z11,0.1, 1, 0.1,1)
print('значения 2 функции')
f1(z2,z22,pi/5,pi,pi/25,0)
