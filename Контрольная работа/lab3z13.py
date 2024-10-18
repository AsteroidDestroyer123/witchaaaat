# из массива убрать все повторяющиеся элементы

n=input('Введите элементы списка через пробел. Когда закончите нажмите enter').split(' ')
m=[]
for i in n:
    if i in m:
        m.remove(i)
    m.append(i)

print(m)