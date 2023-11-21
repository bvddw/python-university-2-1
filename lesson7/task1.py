import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 6 * np.cbrt(6 * (x - 3) ** 2) / (x ** 2 - 2 * x + 9)


plt.close('all')
x = np.linspace(-6, 6, 121)
y = f(x)
x1 = np.linspace(-6, 6, 13)
y1 = f(x1)
Z = np.vstack((x1, y1)).T
print(Z)
plt.plot(x, y, 'r', x1, y1, 'bo-', linewidth=2)
plt.axhline(color='black', lw=3)
plt.axvline(color='black', lw=3)
plt.show()
