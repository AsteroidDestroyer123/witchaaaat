c=''
s=[]
p=[]
print('напишите поочередно для каждого студента 4 результата экзаменов. потом напишите stop')
while c!='stop':
    c=input()
    p.append(c)
p.pop(-1)
for i in p:
    s.append(int(i))
neud=0
c=0
for i in range(0,len(s)-3,4):
    if s[i] == 2 or s[i+1] == 2 or s[i+2] == 2 or s[i+3]==2:
        neud+=1
for i in s:
    c+=i
print(neud,(c/len(s)))