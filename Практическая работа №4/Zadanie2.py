#Напишите программу построения графика по имеющемуся дискретному набору известных значений
import matplotlib.pyplot as plt
import numpy as np
with open('zna4X.txt','r') as f:
    x1=f.readline()
with open('zna4Y.txt','r') as f1:
    y1=f1.readline()
def func(x):#функция преобразуюащя массив со строками в массив с числами с плавующей запятой
    t=[]
    for i in x:
        t.append(float(i))
    return t
x=[]
y=[]
x=x1.split(' ')# разделение строки с значениями х в массив
y=y1.split(' ')# разделение строки с значениями у в массив

x[-1]='80'
x=func(x)
y=func(y)
y1=np.array(y)#преобразование массива в массив np
x1=np.array(x)
print(x1)
fig,ax=plt.subplots()
plt.scatter(x1,y1,c='r')#сам график

plt.show()
