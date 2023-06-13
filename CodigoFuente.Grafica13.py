import matplotlib.pyplot as plt
import numpy as np

θ = np.arange(0, 2*np.pi, 0.015)

r = -250 * np.sin(5*θ) * np.cos(4*θ)
λ = θ + np.sin(r/100)

x = 320 + r * np.cos(λ)
y = -240 - r * np.sin(λ)
fig = plt.figure(facecolor='black')
plt.axis('equal')
plt.axis('off')

plt.plot(x, y, color='red')

plt.show()
