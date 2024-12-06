# Был проведен опрос с тремя вопросами:
#     Какое животное связываете с японией?
#     Какая черта характера присуща японцам больше всего?
#     Какой неодушевленный предмет или понятие связываете с Японией?
# составить программу получения результатов первых пяти наиболее часто встречающихся ответов на вопрос и к каждому написать % частоты встречания 
# ответа на вопрос может не быть у какого либо опрошенного
class MyClass:
    instances = []

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        MyClass.instances.append(self)

    @classmethod
    def get_a(cls):
        all_attributes = []
        for instance in cls.instances:
            all_attributes.append(instance.a)  
        return all_attributes

    @classmethod
    def get_b(cls):
        all_attributes = []
        for instance in cls.instances:
            all_attributes.append(instance.b)  
        return all_attributes

    @classmethod
    def get_c(cls):
        all_attributes = []
        for instance in cls.instances:
            all_attributes.append(instance.c)  

        return all_attributes
n=int(input('Введите колличество опрошенных'))
print('Если ответа на вопрос нет напишите "-"')
for i in range(1,n+1):
    classname=f'Class{i}'
    classname=MyClass(input(f'Введите ответ на 1 вопрос {i} опрошенного'),input(f'Введите ответ на 2 вопрос {i} опрошенного'),input(f'Введите ответ на 3 вопрос {i} опрошенного'))
q1=[]
q2=[]
q3=[]
# Получаем атрибуты всех объектов
attributes = MyClass.get_a()
for i, attrs in enumerate(attributes, 1):
    if attrs!='-':
        q1.append(attrs)
attributes = MyClass.get_b()
for i, attrs in enumerate(attributes, 1):
    if attrs != '-':
        q2.append(attrs)
attributes = MyClass.get_c()
for i, attrs in enumerate(attributes, 1):
    if attrs != '-':
        q3.append(attrs)
def fianl(q1):
    q1p=list(set(q1))
    q1d=dict()
    for i in range(len(q1p)):
        q1d.update({f'{q1p[i]}': f'{round(q1.count(q1p[i])/len(q1),2)*100}'})

    q1dsort=[]
    for i in q1d.values():
        q1dsort.append(float(i))
    q1dsort.sort(reverse=True)

    final1=[]
    for i in q1dsort:
        keys=[key for key, value in q1d.items() if value == str(i)]
        for p in range(len(keys)):
            final1.append(f'{keys[p]}:{i}')
    final1=list(set(final1))
    while len(final1)>5:
        final1.pop(-1)


    return final1
print('Какое животное связываете с японией?')
for i in fianl(q1):
    print(i)
print('Какая черта характера присуща японцам больше всего?')
for i in fianl(q2):
    print(i)
print('Какой неодушевленный предмет или понятие связываете с Японией?')
for i in fianl(q3):
    print(i)