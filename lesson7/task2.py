import numpy as np
from matplotlib import pyplot as plt

plt.close('all')


def f1(x):
    return np.sin(x)


def f2(x):
    return np.exp(-x ** 2)


def f3(x):
    return 1 / (1 + x ** 2)


a = 1
b = 5


def f(x):
    return np.piecewise(x,
                        [x <= a, np.logical_and(x > a, x <= b), x > b],
                        [lambda t: f1(t) - f1(a),
                         lambda t: f2(t) - f2(a),
                         lambda t: f3(t) - f3(b) + f2(b) - f2(a)])


def F(x, y):
    return - x ** 2 - y ** 2 - 4 * x * y - 4 * x - 2 * y + 2


x = np.linspace(-10, 10, 101)
y = f(x)
fig, axes = plt.subplots(1, 2)
fig.set_size_inches(7, 3)
axes[0].plot(x, y, lw=3, c='k')
axes[0].grid(True)

t = np.linspace(-4, 4, 201)
X, Y = np.meshgrid(t, t)
axes[1].set_xlim(-4, 4)
axes[1].set_ylim(-4, 4)
axes[1].contour(X, Y, F(X, Y), [0], linewidths=3, colors='red')
axes[1].grid(True)
plt.show()