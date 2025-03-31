#Напишите программу, строящую график функции. Коэффициенты a,b,c и диапазон задаются с клавиатуры.
# a+bx^2+c*arctan(x)
import matplotlib.pyplot as plt
import numpy as np

a=12#коэффицент а
b=0.3# -//- b
c=3#-//- c
rang1=-10#начало диапазона
rang2=10#конец диапазона

x=np.linspace(rang1,rang2,abs(rang2-rang1)*10)#массив с значениями х
y=a+b*x**2+c*np.arctan(x)#массив с значениями функции
fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()