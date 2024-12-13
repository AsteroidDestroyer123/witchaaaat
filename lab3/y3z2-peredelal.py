#в одномерном массиве увеличить максимальные элементы на их порядковые номера
m=input('вводите числа, которые войдут в массив, через пробел ').split(' ')
k=[]
for i in m:
    k.append(int(i))


p=[]
p.append(k[0])
k[0]+=1
print(p)
for i in range(1,len(k)):
    c = k[i]
    if k[i]>max(p):

        k[i]+=(1+i)
    p.append(c)


print(k)