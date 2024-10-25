#в одномерном массиве увеличить максимальные элементы на их порядковые номера
m=input('вводите числа, которые войдут в массив, через пробел').split(' ')
k=[]
for i in m:
    k.append(int(i))


ans=[]
c=1
p=k[0]-1
for i in k:
    if i>p:
        p=i
        ans.append(i+c)
    else:
        ans.append(i)
    c+=1
print(ans)
