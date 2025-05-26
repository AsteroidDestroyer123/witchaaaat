import numpy as np
import matplotlib.pyplot as plt


def gradspusk(func=lambda x: np.exp(-x**2),
                    diffFunc=lambda x: -2*x*np.exp(-x**2),
                    x0=3,
                    speed=0.1,
                    epochs=1000):
    x = x0
    x_list = [x]
    y_list = [func(x)]
    
    for i in range(epochs):
        x = x + speed * diffFunc(x)
        x_list.append(x)
        y_list.append(func(x))
    
    return x_list, y_list


func = lambda x: np.exp(-x**2)
diffFunc = lambda x: -2*x*np.exp(-x**2)


x0 = 3
speed = 1
epochs = 500
x_list, y_list = gradspusk(func, diffFunc, x0, speed, epochs)


x = np.linspace(-5, 5, 400)
y = func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)', color='blue')
plt.scatter(x_list, y_list, color='red',s=20)
plt.scatter(x_list[-1],y_list[-1],marker='*',s=200)
plt.legend()
plt.grid(True)
plt.show()

#Граничное значение параметра speed равно 1