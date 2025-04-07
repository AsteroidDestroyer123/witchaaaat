import numpy as np
import matplotlib.pyplot as plt
from random import randint,uniform
n = 100
a=0.01
b=0.01

k_ideal = 2    
b_ideal = 1    
x1 = np.linspace(0, 10, n)

noise = np.random.normal(0, 2, size=n)  
y1 = k_ideal * x1 + b_ideal + noise



k_pred=uniform(0,5)
b_pred=uniform(0,5)
for l in range(100000):
    yi=[]
    for i in x1:
        yi.append(k_pred*i+b_pred)

    djdk_pred=0
    for i in range(len(x1)):
        djdk_pred+=(x1[i]*(y1[i]-yi[i]))
    djdk=(-2/n)*djdk_pred

    djdb_pred=0
    for i in range(len(x1)):
        djdb_pred+=((y1[i]-yi[i]))
    djdb=(-2/n)*djdb_pred

    k_new=k_pred-a*(djdk)
    b_new=b_pred-b*(djdb)
    k_pred=k_new
    b_pred=b_new
print(k_new,b_new)  
plt.scatter(x1, y1, s=10)
plt.plot(x1, k_ideal * x1 + b_ideal, 'g--', label="Истинная прямая")
plt.plot(x1, k_pred * x1 + b_pred, 'r', label="Прогноз")
plt.legend()
plt.show()