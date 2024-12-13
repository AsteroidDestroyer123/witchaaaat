#минимальный элемент одномерного массива увеличить в два раза
m=input('вводите числа, которые войдут в массив, через пробел').split(' ')
k=[]
for i in m:
    k.append(int(i))

n=min(k)
for i in range(len(k)):
    if k[i]==n:
        k[i]*=2
print(k)