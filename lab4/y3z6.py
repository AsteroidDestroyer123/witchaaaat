#дана матрица n x n. сформировать два массива в 1-ом элементы верхнего треугольника с элемнтом главной диагонали
import numpy as np

n = 4
a = np.array([[1, 2, 3, 4], [11, 22, 33, 44], [111, 222, 333, 444], [1111, 2222, 3333, 4444]])
x = []
y = []
p = n
c = 1
while p > 0:
    for i1 in range(c):
        for i2 in range(p):
            x.append(int(a[i1, i2]))
    p -= 1
    c += 1
for i1 in range(n):
    for i in range(n):
        if a[i1, i] not in x:
            y.append(int(a[i1, i]))
print(set(x))
print(y)

