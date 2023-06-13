import matplotlib.pyplot as plt
import numpy as np

# Generar valores de θ desde 0 hasta 2π con un paso de 0.01
θ = np.arange(0, 2*np.pi, 0.01)

# Calcular los valores de r utilizando las ecuaciones
r = 2 - 2*np.sin(θ) + np.sin(θ) * np.sqrt(np.abs(np.cos(θ))/np.sin(θ) + 1.4)

# Calcular los valores de x y y utilizando las ecuaciones polares
x = r * np.cos(θ)
y = r * np.sin(θ)

# Creacion de la figura con fondo negro
fig = plt.figure(facecolor='black')

# Graficar el área rellenada entre x y y con color rojo
plt.fill_between(x, y, color='red')

# Establecer los ejes x y y con escala igual y sin mostrar los ejes
plt.axis('equal')
plt.axis('off')

# Mostrar la gráfica
plt.show()
