#в одномерном массиве увеличить максимальные элементы на их порядковые номера
m=input('вводите числа, которые войдут в массив, через пробел ').split(' ')
k=[]
for i in m:
    k.append(int(i))


mx=max(k)
for i in range(len(k)):
    if k[i]==mx:
        k[i]=k[i]+i+1
print(k)