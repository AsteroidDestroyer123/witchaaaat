#2.В компьютер вводятся по очереди координаты и точек. Опреде-лить, сколько из них попадет в круг радиусом г с центром в точке (а, b).

r=int(input('радиус'))
x=int(input('центр радиус по x'))
y=int(input('центр радиуса по y'))
c=''
p=[]
s=[]
while c!='stop':
    c=input()
    p.append(c)
p.pop(-1)
for i in p:
    s.append(int(i))

k=0
for i in range(0,len(s)-1,2):
    if (s[i]-x)**2+(s[i+1]-y)**2<=r**2:
        k+=1
print(k)