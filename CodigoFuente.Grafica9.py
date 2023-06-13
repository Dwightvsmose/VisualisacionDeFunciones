import numpy as np
import matplotlib.pyplot as plt

# definicion de las funciones
def x(t):
    return np.cos(t)**3

def y(t):
    return np.sin(t)**3

# indicacion de valores t
t = np.linspace(0, 2*np.pi, 100)

# Evaluacion de las funciones por cada valor t
x_values = x(t)
y_values = y(t)

# Creacion de plot
plt.plot(x_values, color='b', label='x = cos^3(t)')
plt.plot(y_values, color='r', label='y = sin^3(t)')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Grafica de x = cos^3(t) y y = sin^3(t)')
plt.axhline(y=0, color='black', linewidth=0.5)  # eje x
plt.axvline(x=0, color='black', linewidth=0.5)  # eje y
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()

# Mostrar Plot
plt.show()
