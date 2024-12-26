import numpy as np
def bubble(b):  
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(b) - 1):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                swap_bool = True
    return b

def f(a):
    sh=a.shape[0]
    for i in range(sh):  
        if (i+1) % 2 == 0:  
            a[i] = bubble(a[i]) 
        else:  
            a[i] = bubble(a[i])[::-1]  
    return a


a = np.array([
    [43, 62, 7],
    [3, 123, 32],
    [56, 8, 4],
    [232, 23, 41]
    ])


print(f(a))