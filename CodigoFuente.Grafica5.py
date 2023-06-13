import numpy as np
import matplotlib.pyplot as plt

# Definicion de las funciones s(x) y v(x)
def s(x):
    return np.cos(2*x) + np.sin(3*x)

def v(x):
    return -2*np.sin(2*x) + 3*np.cos(3*x)

# Generacion de valores de x de 0 a 4π con 200 points
x = np.linspace(0, 4*np.pi, 200)

# Evaluacion de s(x) y v(x) para cada valor x
y_s = s(x)
y_v = v(x)

# plot
plt.plot(x, y_s, color='blue', label='s(x) = cos(2x) + sin(3x)')
plt.plot(x, y_v, color='red', label='v(x) = -2sin(2x) + 3cos(3x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de s(x) and v(x)')
plt.axhline(y=0, color='black', linewidth=0.5) 
plt.axvline(x=0, color='black', linewidth=0.5) 
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()

# muestra de plot
plt.show()
