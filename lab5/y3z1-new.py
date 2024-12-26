from math import cos,sin,pi,e,factorial
import numpy as np
def f1(a,b,h):
    for x in np.arange(a,b,h):
        delta2=-1000
        delta1=(e**(cos(x)))*cos(sin(x))
        c=1
        i=0
        while delta1 != delta2:
            a=(round(cos(i*x),10))/(round(factorial(i),10))
            delta2=round(a,10)
            c+=delta2
            i+=1
    return c
print(f1(0.1,1,0.1))