import matplotlib.pyplot as plt
import numpy as np

# Generar valores de x desde 0.0 hasta 2 con un paso de 0.01
x = np.arange(0.0, 2, 0.01)

# Calcular los valores de y1 e y2
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

# Crear el primer subplot
plt.subplot(3, 1, 1)
plt.fill_between(x, 0, y1)  # Rellenar el área entre y1 y 0
plt.ylabel('entre y1 y 0')

# Crear el segundo subplot
plt.subplot(3, 1, 2)
plt.fill_between(x, y1, 1)  # Rellenar el área entre y1 y 1
plt.ylabel('entre y1 y y2')

plt.xlabel('x')  # Establecer la etiqueta del eje x

plt.show()

