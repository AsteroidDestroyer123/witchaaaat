#Соревнования по фоутболу проводяится в 2 этапа.
#1 этап: 24 команды пазбиваются нв 2 группы по 12 и по 6 лучших команд из каждой группы выходят во 2 этап
#Нужно составить таблицу участников 2 этапа
from prettytable import PrettyTable
print('Вводите метса в команд от первой до последней в первой группе(1 место самое крутое)')
class group1:
    t1=(int(input('Введите место 1 команды среди всей первой группы')))
    t2=(int(input('Введите место 2 команды среди всей первой группы')))
    t3=(int(input('Введите место 3 команды среди всей первой группы')))
    t4=(int(input('Введите место 4 команды среди всей первой группы')))
    t5=(int(input('Введите место 5 команды среди всей первой группы')))
    t6=(int(input('Введите место 6 команды среди всей первой группы')))
    t7=(int(input('Введите место 7 команды среди всей первой группы')))
    t8=(int(input('Введите место 8 команды среди всей первой группы')))
    t9=(int(input('Введите место 9 команды среди всей первой группы')))
    t10=(int(input('Введите место 10 команды среди всей первой группы')))
    t11=(int(input('Введите место 11 команды среди всей первой группы')))
    t12=(int(input('Введите место 12 команды среди всей первой группы')))
        
def get_top_attributes(cls, top_n=6):
    attributes = {attr: getattr(cls, attr) for attr in dir(cls) if not attr.startswith('__') and not callable(getattr(cls, attr))}
    sorted_attributes = sorted(attributes.items(), key=lambda item: item[1], reverse=False)
    return sorted_attributes[:top_n]
print('Вводите метса в команд от первой до последней во второй группе(1 место самое крутое)')
class group2:
    t13=(int(input('Введите место 13 команды среди всей второй группы')))
    t14=(int(input('Введите место 14 команды среди всей второй группы')))
    t15=(int(input('Введите место 15 команды среди всей второй группы')))
    t16=(int(input('Введите место 16 команды среди всей второй группы')))
    t17=(int(input('Введите место 17 команды среди всей второй группы')))
    t18=(int(input('Введите место 18 команды среди всей второй группы')))
    t19=(int(input('Введите место 19 команды среди всей второй группы')))
    t20=(int(input('Введите место 20 команды среди всей второй группы')))
    t21=(int(input('Введите место 21 команды среди всей второй группы')))
    t22=(int(input('Введите место 22 команды среди всей второй группы')))
    t23=(int(input('Введите место 23 команды среди всей второй группы')))
    t24=(int(input('Введите место 24 команды среди всей второй группы')))
def get_top_attributes(cls, top_n=6):
    attributes = {attr: getattr(cls, attr) for attr in dir(cls) if not attr.startswith('__') and not callable(getattr(cls, attr))}
    sorted_attributes = sorted(attributes.items(), key=lambda item: item[1], reverse=False)
    return sorted_attributes[:top_n]

top_attributes1 = get_top_attributes(group1, top_n=3)
finallist=dict()
for name, value in get_top_attributes(group1, top_n=6):
    finallist.update({f"{name}": f"{value}"})
for name, value in get_top_attributes(group2, top_n=6):
    finallist.update({f"{name}": f"{value}"})
print('Название команды и место в своей группе')
table=PrettyTable()
table.field_names=['Название команды','Место в группе']
for i,j in finallist.items():
    table.add_row([i,j])
print(table)
