#поменять местами столбец, содержащий максимальный элемент на главной диагонал
#квдаратной матрицы со столбцом содержащим максимальный элемент первой строки
import numpy as np
a=np.array([[1,23,51,8],
            [23,14,2,6],
            [23,1,5,23],
            [23,12,6,9]
            ])
def f(a):
    
    size=a.shape[0]
    mx1=a[0][0]
    j1=0
    for i in range(size):
        if a[i][i]>mx1:
            j1=i
            mx1=a[i][i]
    
    mx2=a[0][0]
    j2=0
    for i in range(size):
        if a[0][i]>=mx2:
            j2=i
            mx2=a[0][i]
    if j1==j2:
        for i in range(size):
            if i!=j1:
                if a[0][i]>=mx2:
                    j2=i
                    mx2=a[0][i]
    for i in range(size):
        a[i][j1], a[i][j2]= a[i][j2], a[i][j1]
    return a
#пример
a=np.array([[51,23,51,8],
            [23,14,2,6],
            [23,1,5,23],
            [23,12,6,9]
            ])
print(f(a))
