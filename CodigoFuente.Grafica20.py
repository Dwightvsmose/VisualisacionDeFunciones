import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1.1, 0.1)
y = np.arange(-1, 1.1, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.cos(np.abs(X) + np.abs(Y)) * (np.abs(X) + np.abs(Y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
