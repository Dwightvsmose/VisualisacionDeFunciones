import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return t + 2*np.sin(2*t)

def y(t):
    return t + 2*np.cos(5*t)

t = np.linspace(-2*np.pi, 2*np.pi, 100)

x_values = x(t)
y_values = y(t)
 
plt.plot(x_values, color='c', label='x = t + 2sin(2t)')
plt.plot(y_values, color='m', label='y = t + 2cos(5t)')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Grafica de x = t + 2sin(2t) y y = t + 2cos(5t)')
plt.axhline(y=0, color='white', linewidth=0.5)  
plt.axvline(x=0, color='white', linewidth=0.5)  
plt.grid(True, linestyle='--', linewidth=0.5, color='white')
plt.legend()

plt.show()
