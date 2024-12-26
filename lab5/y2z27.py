#в матрице максимальные элементы четных строк заменить на 0, а нечетных умножить на мномер столбца
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
                    a[i,j]=a[i,j]*(j+1)
    return a
#пример
a=np.array([[1,23,51,8,43],
            [23,14,2,6,43],
            [23,1,5,23,9]
            ])
b=np.array([[14,45,23,6,34],
            [4,654,1,32,6],
            [283,2,1,243,1]
            ])
print(f(a))
print(f(b))
