import matplotlib.pyplot as plt
import numpy as np

# Generar los valores de x y y en el rango [-2, 2] con un incremento de 0.2
x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)

# Crear una malla de coordenadas x y y utilizando np.meshgrid
X, Y = np.meshgrid(x, y)

# Calcular los valores de z utilizando la función 
Z = X**2 - Y**2

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Establecer etiquetas de los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Mostrar la gráfica
plt.show()
