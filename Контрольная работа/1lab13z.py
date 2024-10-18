# составть таблицу значений y=1,x<=-1,y=-x,-1<x<1,y=-1,x>1 на отрезек -1.5<=x<=1.5 с шагом h=0.1
import numpy as np
m=[]
for i in np.arange(-1.5,1.6,0.1):
    x=round(i,2)
    x=float(x)
    if x<=-1:
        m.append(1)
    elif x==0:
        m.append(0)
    elif -1<x<1:
        m.append(-1*x)
    else:
        m.append(-1)
print(m)