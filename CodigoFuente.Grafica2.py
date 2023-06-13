import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return 2*x**2 - 8*x - 11

x = np.linspace(-1, 5, 100)

y = g(x)

plt.plot(x, y, color='red', label='g(x) = 2x^2 - 8x - 11')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Grafica de g(x) = 2x^2 - 8x - 11')
plt.axhline(y=0, color='black', linewidth=0.5) 
plt.axvline(x=0, color='black', linewidth=0.5)  
plt.grid(True, linestyle='--', linewidth=0.5)

plt.show()
