import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**2
    return y

x = np.linspace( -5 , 5, 100)
#y = f(x)
y2 = (x - 3)**2
y = x**3

plt.plot(-x , y)
#plt.plot(x, -y)
#plt.plot(x, y+3)
#plt.plot(x, y2)
plt.grid()
plt.show()

