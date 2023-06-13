import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return (1 + 2*np.sin(t)) * np.cos(t)

def y(t):
    return (1 + 2*np.sin(t)) * np.sin(t)

t = np.linspace(0, 2*np.pi, 100)

x_values = x(t)
y_values = y(t)

plt.plot(x_values, y_values, color='cyan', label='x(t) = (1+2sin(t))*cos(t)')
plt.plot(x_values, y_values, color='magenta', label='y(t) = (1+2sin(t))*sin(t)')
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Grafica de x(t) e y(t)')
plt.axhline(y=0, color='white', linewidth=0.5) 
plt.axvline(x=0, color='white', linewidth=0.5) 
plt.grid(True, linestyle='--', linewidth=0.5, color='white')
plt.legend()

plt.show()
