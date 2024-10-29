#сформировать матрицу n x 3n составленую 
# из трех единичных квадраных матриц n x n
import numpy as np
n=int(input('введите n'))
a=np.ones((n,n))
b=np.array((a,a))
print(a)
print(b)