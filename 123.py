# 2 уровень 1 задание
from math import cos,factorial
s=0 
x=1
n=1
e=113123
while abs(e)> 0.0001:
    e=cos(n*x)/(n**n)
    s=s+e
    n+=1
print(s)
# 2 уровень 1 задание 

L=1
n=1
while L <= 30000:
    L=1
    for i in range(1,n+1,3):
        L*=i
    n+=3
else:
    print(n-6)
# 3 уровень 1 задание
# e=12313
# s1=0
# s=0
# while abs(e) > 0.0001:
#     x=0.1
#     i=1
#     while x<1:

#         e=((-1)**i)*((x**(2*i))/(factorial(2*i)))
#         s=s+e
#         x+=0.1
#         s1=s1+cos(x)
#     i+=1
# print(s,s1)
