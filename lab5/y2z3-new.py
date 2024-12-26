import numpy as np
b=np.array([[1,23,51,8,4],
            [23,14,2,6,9],
            [23,1,5,23,43],
            [23,12,6,9,22],
            [32,54,12,2,64]
            ])
c=np.array([[6,23,551,38,4,45],
            [23,134,2,26,39,53],
            [2113,1,555,23,43,4],
            [233,12,6,879,22,45],
            [32,54,12,2,64,12],
            [43,6,52,44,27,8],
            ])
def f(a):
    size=a.shape[0]
    mx2=a[0][0]
    j2=0
    for i in range(size):
        if a[i][i]>=mx2:
            j2=i
            mx2=a[i][i]
    a=np.delete(a, j2, axis=0)
    return a
print(f(c))
print(f(b))