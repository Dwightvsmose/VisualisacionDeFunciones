import matplotlib.pyplot as plt
import numpy as np

# Generar los valores de x e y en el rango [-10, 10] con un incremento de 5
x = np.arange(-10, 11, 5)
y = np.arange(-10, 11, 5)

# Crear una malla de coordenadas x e y utilizando np.meshgrid
X, Y = np.meshgrid(x, y)

# Calcular los valores de z utilizando la función z = sin(|x| - |y|)
Z = np.sin(np.abs(X) - np.abs(Y))

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie utilizando plot_trisurf
ax.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap='viridis')

# Establecer etiquetas de los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Mostrar la gráfica
plt.show()
