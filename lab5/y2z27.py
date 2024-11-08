#в матрице максимальные элементы четных строк заменить на 0, а нечетных умножить на мномер столбца(я считал что нумерация столбцов начинается с 0)
import numpy as np

def f(a):
    for i in range(a.shape[0]):
        t=max(a[i])
        if (i+1)%2==0:
            for j in range(a.shape[1]):
                if a[i,j] == t:
                    a[i,j]=0
        else:
            for j in range(a.shape[1]):
                if a[i,j] == t:
                    a[i,j]=a[i,j]*j
    return a
#пример
a=np.array([[1,23,51,8,43],
            [23,14,2,6,43],
            [23,1,5,23,9]
            ])
print(f(a))