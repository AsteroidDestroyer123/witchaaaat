# В группе учатся n студентов. Каждый сдал 4 экзамена. Подсчитать число неуспевающих студентов и средний бал.
n=int(input('введите чмло студентов: '))
m=[]
for i in range(n*4):
    m.append(int(input('введите оценку студента: ')))
c=0

for i in range(0,len(m)-3,4):
    if m[i]==2 or m[i+1] == 2 or m[i+2]==2 or m[i+3] == 2:
        c+=1
sr=0
for i in m:
    sr+=i
sr=sr/(4*n)
print(c,sr)