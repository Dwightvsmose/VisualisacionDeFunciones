import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 2, 1)
y = np.arange(-1, 2, 1)

X, Y = np.meshgrid(x, y)

Z = np.cos(np.abs(X) - np.abs(Y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
