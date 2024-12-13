#Поменять местами сосдение элементы перед максимальным(1 с 2, 3 с 4)
m=input('вводите числа, которые войдут в массив, через пробел').split(' ')
k=[]
for i in m:
    k.append(int(i))


c=k.index(max(k))
if c%2==0:
    for i in range(0,c-1,2):
        k[i],k[i+1]=k[i+1],k[i]
else:
    for i in range(0,c-2,2):
        k[i],k[i+1]=k[i+1],k[i]

print(k)