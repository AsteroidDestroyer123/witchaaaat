import matplotlib.pyplot as plt
import numpy as np
with open('zna4X.txt','r') as f:
    x1=f.readline()
with open('zna4Y.txt','r') as f1:
    y1=f1.readline()
def func(x):
    t=[]
    for i in x:
        t.append(float(i))
    return t
sizes=100
colors='red'
x=[]
y=[]
x=x1.split(' ')
y=y1.split(' ')

x[-1]='80'
x=func(x)
y=func(y)
y1=np.array(y)
x1=np.array(x)
print(x1)
print(y1)
fig,ax=plt.subplots()
plt.scatter(x1,y1,c='r')

plt.show()