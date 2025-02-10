with open("massivA.txt", "w", encoding="utf-8") as file_a:
    file_a.write("whieefwhiefwhiohiwefihewfoiddjkjsd")
with open("massivB.txt", "w", encoding="utf-8") as file_b:
    file_b.write("MEFMWKNSDKMSDKMMSAFWO;EOKSADFLK;")
with open("massivA.txt", "r") as file_a:
    a = file_a.read() 
with open("massivB.txt", "r") as file_a:
    b = file_a.read() 
k=5
with open("massivA.txt","w") as f:
    f.write(a[:k]+b+a[k:])
with open("massivA.txt",'r') as f:
    result=f.read()
print(result)

