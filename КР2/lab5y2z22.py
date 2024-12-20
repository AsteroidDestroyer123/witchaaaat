#Для матрицы составить два одномерных массива
#1 массив: колличество отрицательных элементов строк
#2 массив: максимальные среди отрицательных элементов столбцов
import numpy as np
a=np.array([[5,-6,4,-10,-5],
            [6,-3,-8,34,-9],
            [0,-7,32,34,-8]])
result_strok=[]
result_stolb=[]
for i in range(np.shape(a)[0]):
    c=0
    for j in range(np.shape(a)[1]):
        if a[i][j]<0:
            c+=1
    result_strok.append(c)
for i in range(np.shape(a)[1]):
    c=0
    p=[]
    for j in range(np.shape(a)[0]):
        if a[j][i]<0:
            p.append(a[j][i].item())
    if p == []:
        result_stolb.append('Отицательные элементы отсутствуют')
    else:
        result_stolb.append(max(p))
print(result_strok,result_stolb)
