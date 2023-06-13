import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.exp(-3*x)

def g(x):
    return np.exp(-3*x) * (1 - 3*x)

x = np.linspace(0, 2, 200)

y1 = f(x)
y2 = g(x)

plt.plot(x, y1, 'c-', label='f(x) = xe^-3x')
plt.plot(x, y2, 'm-', label='g(x) = e^-3x(1-3x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica para f(x) y g(x)')
plt.legend()
plt.grid(True)

plt.show()
