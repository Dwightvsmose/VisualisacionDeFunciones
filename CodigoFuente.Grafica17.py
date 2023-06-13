import matplotlib.pyplot as plt
import numpy as np

# Generar los valores de x y y en el rango [-5, 5] con un incremento de 1
x = np.arange(-5, 6, 1)
y = np.arange(-5, 6, 1)

# Crear una malla de coordenadas x y y utilizando np.meshgrid
X, Y = np.meshgrid(x, y)

# Calcular los valores de z utilizando la función z = |cos(x) + cos(y)|^(1/2)
Z = np.abs(np.cos(X) + np.cos(Y))**(1/2)

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie utilizando plotwireframe
ax.plot_wireframe(X, Y, Z)

# Establecer etiquetas de los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Mostrar la gráfica
plt.show()
