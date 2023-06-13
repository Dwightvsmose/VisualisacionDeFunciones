import numpy as np
import matplotlib.pyplot as plt

# Definicion De Funcion
def f(x):
    return 5 - 4*x - x**2

# Valores de x
x = np.linspace(-6, 2, 200)

# Calculo de valores
y = f(x)

# Creacion de Grafica
plt.plot(x, y, color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafica de f(x) = 5 - 4x - x^2')
plt.grid(True)

# Muestra de Grafica
plt.show()
