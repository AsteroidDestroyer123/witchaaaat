# 5 судей оценивую 120 метровый прыжок с трамплина на лыжах по 20ти бальной шкале.Меньшая и большая оценки отбрасываются,
#а остальные суммируются и к этой сумме прибавляются очки за дальность прыжка: за 60-120м прибавляются по 2 очка за каждый метр
#за 0-60 отнимаются 2 очка за каждый метр
#Получить таблицу с фамилией и результатом каждого участника
def delminmax(x):
    min1 = min(x)
    max1 = max(x)
    return [item for item in x if item != min1 and item != max1]
num_of_smen=int(input('Введите колличество спортменов'))
class smen():
    all_objects=[]
    def __init__(self,name,result) -> None:
        self.name=name
        self.result=result
        smen.all_objects.append(self)

    def pr(self):
        for i,j in self.__dict__.items():
            print(f'{i}:{j}')
    @classmethod
    def print_all_objects(cls):
        for i in cls.all_objects:
            i.pr()
def ocen():
    name=input('Введите имя спортсмена: ')
    dist=int(input('Введите димтанцию спортсмена:'))
    
    m=[]
    for i in range(5):
        m.append(int(input(f'Введите оценку {i+1} судьи: ')))
    m=delminmax(m)
    if dist > 120:
        m.append(60+((dist)-120)*2)
    else:
        m.append(60-(abs((dist)-120)*2))
    name=smen(name,sum(m))
    return name
for i in range(num_of_smen):
    ocen()
smen.print_all_objects()
