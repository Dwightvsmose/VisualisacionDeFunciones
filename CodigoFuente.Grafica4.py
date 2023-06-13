import numpy as np
import matplotlib.pyplot as plt

def h(t):
    return np.exp(0.1*t) * np.sin(2*t)

t = np.linspace(0, 24, 250)

y = h(t)

plt.figure(facecolor='black')
plt.plot(t, y, color='c', linewidth=1.5, label='h(t) = e^(0.1t) * sin(2t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Grafica de h(t) = e^(0.1t) * sin(2t)', color='white')
plt.axhline(y=0, color='white', linewidth=0.5)  # Add x-axis
plt.axvline(x=0, color='white', linewidth=0.5)  # Add y-axis
plt.grid(True, linestyle='--', linewidth=0.5, color='white')
plt.legend()
plt.xticks(color='white')
plt.yticks(color='white')
plt.gca().set_facecolor('black')
plt.rcParams['lines.markersize'] = 2

plt.show()
