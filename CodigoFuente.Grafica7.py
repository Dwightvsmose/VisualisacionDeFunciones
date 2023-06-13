import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.sin(3*t) * np.cos(2*t)

def g(t):
    return 0.5 * np.cos(t) + 2.5 * np.cos(5*t)

t = np.linspace(0, 4*np.pi, 100)

y_f = f(t)
y_g = g(t)

plt.plot(t, y_f, color='cyan', label='f(t) = sin(3t) * cos(2t)')
plt.plot(t, y_g, color='magenta', label='g(t) = 1/2 * cos(t) + 5/2 * cos(5t)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica f(t) y g(t)')
plt.axhline(y=0, color='black', linewidth=0.5) 
plt.axvline(x=0, color='black', linewidth=0.5) 
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()

plt.show()
