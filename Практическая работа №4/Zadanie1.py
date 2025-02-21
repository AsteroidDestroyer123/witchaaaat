#a+bx^2+c*arctan(x)
import matplotlib.pyplot as plt
import numpy as np

a=2#коэффицент а
b=1# -//- b
c=3#-//- c
rang1=-10#начало диапазона
rang2=10#конец диапазона

x=np.linspace(rang1,rang2,abs(rang2-rang1)*10)
print(x)
y=a+b*x**2+c*np.arctan(x)
fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()