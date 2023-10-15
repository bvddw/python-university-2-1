import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')


def f(x):
    return np.piecewise(x,
                        [x <= 3],
                        [lambda t: 3 - t, lambda t: 0])


def F1(x, y):
    return f(np.sqrt(x ** 2 + y ** 2))


def F2(x, y):
    return f(np.abs(x))


x = np.linspace(-4, 4, 81)
z = f(np.abs(x))

# Create a single figure
fig = plt.figure(figsize=(12, 6))

axUpLeft = plt.subplot2grid((2, 2), (0, 0))
axUpLeft.plot(x, z, lw=3, c='k')
axUpLeft.set_title('1D Plot')

X1, Y1 = np.meshgrid(x, x)
Z1 = F1(X1, Y1)

axDown = plt.subplot2grid((2, 2), (0, 1), projection='3d')
axDown.plot_surface(X1, Y1, Z1, rstride=1, cstride=1)
axDown.set_title('Surface Plot')

X2, Y2 = np.meshgrid(x, x)
Z2 = F2(X2, Y2)

axRight = plt.subplot2grid((2, 2), (1, 0), colspan=2, projection='3d')
axRight.plot_wireframe(X2, Y2, Z2, rstride=8, cstride=2, color='b')
axRight.set_title('Wireframe Plot')

plt.show()
