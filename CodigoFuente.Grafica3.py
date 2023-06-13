import numpy as np
import matplotlib.pyplot as plt

# Definicion de la funcion f(t)
def f(t):
    return t * np.exp(2*t)

# Generacion de valores t
t = np.linspace(-1, 5, 300)

# Evaluacion de f(t) por cada valor t
y = f(t)

# Creacion de Plot
plt.plot(t, y, color='k', linewidth=10, label='f(t) = t * e^(2t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Grafica de f(t) = t * e^(2t)')
plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis
plt.axvline(x=0, color='black', linewidth=0.5)  # Add y-axis
plt.grid(True, linestyle='--', linewidth=0.5)

# Muestra de Plot
plt.show()
