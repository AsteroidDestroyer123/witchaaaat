#вычислить сумму эдементов с нечетным индексом, предварительно поменяв попарно элемнты начиная с первого, если первой элемнт больше среднего арифметического всей прогресии 
# и с последнего элемента в противном случае
def perestanovka(p):
    c=0
    x=p.copy()
    for i in x:
        c+=i
    srzn=c/len(x)
    if len(x)%2==0:
            for i in range(0,len(x)-1,2):
                t=x[i]
                p=x[i+1]
                x[i]=p
                x[i+1]=t
    else:
        if x[0]>srzn:
            for i in range(0,len(x)-2,2):
                t=x[i]
                p=x[i+1]
                x[i]=p
                x[i+1]=t
        else:
            for i in range(len(x)-1,2,-2):
                t=x[i]
                p=x[i-1]
                x[i]=p
                x[i-1]=t
    return x

def f(m):
    t=perestanovka(m)
    k=0
    for i in range(len(t)):
        if i%2==1:
            k+=t[i]
    return k


#пример 
m=[6,1,3,9,4,6,8,5,3,1,23,9,6,0,0]

print(f(m))
