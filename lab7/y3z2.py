#Соревнования по фоутболу проводяится в 2 этапа.
#1 этап: 24 команды пазбиваются нв 2 группы по 12 и по 6 лучших команд из каждой группы выходят во 2 этап
#Нужно составить таблицу участников 2 этапа
from prettytable import PrettyTable




class group1:
    t1 = 3
    t2 = 2
    t3 = 1
    t4 = 4
    t5 = 5
    t6 = 6
    t7 = 7
    t8 = 9
    t9 = 8
    t10 = 10
    t11 = 12
    t12 = 1


def get_top_attributes(cls, top_n=6):
    attributes = {attr: getattr(cls, attr) for attr in dir(cls) if
                  not attr.startswith('__') and not callable(getattr(cls, attr))}
    sorted_attributes = sorted(attributes.items(), key=lambda item: item[1], reverse=False)
    return sorted_attributes[:top_n]




class group2:
    t13 = 4
    t14 = 7
    t15 = 2
    t16 = 12
    t17 = 3
    t18 = 1
    t19 = 11
    t20 = 9
    t21 = 10
    t22 = 8
    t23 = 5
    t24 = 6


def get_top_attributes(cls, top_n=6):
    attributes = {attr: getattr(cls, attr) for attr in dir(cls) if
                  not attr.startswith('__') and not callable(getattr(cls, attr))}
    sorted_attributes = sorted(attributes.items(), key=lambda item: item[1], reverse=False)
    return sorted_attributes[:top_n]


top_attributes1 = get_top_attributes(group1, top_n=3)
finallist = dict()
for name, value in get_top_attributes(group1, top_n=6):
    finallist.update({f"{name}": f"{value}"})
for name, value in get_top_attributes(group2, top_n=6):
    finallist.update({f"{name}": f"{value}"})

table = PrettyTable()
table.field_names = ['Название команды', 'Место в группе']
for i, j in finallist.items():
    table.add_row([i, j])
print(table)
