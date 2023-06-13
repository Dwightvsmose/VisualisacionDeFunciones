import matplotlib.pyplot as plt
import numpy as np

# Generar valores de θ desde 0 hasta 4π con un incremento de 0.4
θ = np.arange(0, 4*np.pi, 0.4)

# Calcular los valores de r y λ
r = 105 + 100 * np.sin(4.5*θ)
λ = θ - np.cos(10*θ)/10

# Calcular los valores de x y y
x = 320 + r * np.cos(λ)
y = -240 - r * np.sin(λ)

#Fondo negro
fig = plt.figure(facecolor='black')

# Crear la figura con axis igual y sin mostrar los ejes
plt.axis('equal')
plt.axis('off')

# Graficar x versus y
plt.plot(x, y, color='red')

# Mostrar la gráfica
plt.show()
