n=int(input())
s=[int(input()) for i in range(n)]
c=0
for i in s:
    if i <30:
        c+=400
    else:
        c+=200
print(c/1000)
