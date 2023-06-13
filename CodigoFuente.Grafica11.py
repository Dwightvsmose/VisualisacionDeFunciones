import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.sin(3*t)

def y(t):
    return np.sin(4*t)

t = np.linspace(0, 2*np.pi, 100)

x_values = x(t)
y_values = y(t)
  
plt.plot(x_values, color='cyan', marker='o', markersize=2, label='x = sin(3t)')
plt.plot(y_values, color='magenta', marker='o', markersize=2, label='y = sin(4t)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de x = sin(3t) y y = sin(4t)')
plt.axhline(y=0, color='black', linewidth=0.5)  
plt.axvline(x=0, color='black', linewidth=0.5) 
plt.grid(True, linestyle='--', linewidth=0.5, color='black')
plt.legend()

plt.show()
