#15. Заданы массивы А и В, содержащие n и m элементов соответственно. 
#Вставить массив В между k-м и (k + 1)-м элементами массива А (k задано).
with open("massivA.txt", "r") as file_a:
    a = file_a.read() 
with open("massivB.txt", "r") as file_a:
    b = file_a.read() 
k=5
result = b[:k]+a+b[k:]
print(result)
with open("massivB.txt", "w") as f:
    f.write(result)