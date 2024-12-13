#Найти все максимальные элемента массива за один проход и сформировать мписок с их индексами
m=input('вводите числа, которые войдут в массив, через пробел').split(' ')
k=[]
for i in m:
    k.append(int(i))

mx=max(k)
c=[]
for i in range(len(k)):
    if k[i]==mx:
        c.append(i)

print(c)