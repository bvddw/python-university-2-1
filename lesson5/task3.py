import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(-1, 1, n + 1)
y = np.linspace(-1, 1, n + 1)
[X, Y] = np.meshgrid(x, y)

x0 = -0.4
y0 = -0.4

x1 = -0.4
y1 = 0.35

x2 = -0.15
y2 = 0.6

x3 = 0.15
y3 = 0.6

x4 = 0.4
y4 = 0.35

x5 = 0.4
y5 = -0.4

q1 = Y > y0 + (y5 - y0) / (x5 - x0) * (X - x0)
q2 = X > x1
q3 = Y < y1 + (y2 - y1) / (x2 - x1) * (X - x1)
q4 = Y < y2 + (y3 - y2) / (x3 - x2) * (X - x2)
q5 = Y < y3 + (y4 - y3) / (x4 - x3) * (X - x3)
q6 = X < x5

q = q1 & q2 & q3 & q4 & q5 & q6
B = np.zeros([n + 1, n + 1])
B[np.flipud(q)] = 255

cc = 128
w = 5
B[0:w, :] = cc
B[-w:, :] = cc
B[:, :w] = cc
B[:, -w:] = cc
ext = [-1, 1, -1, 1]
plt.imshow(B, cmap='gray', extent=ext)
plt.savefig('my_image.png', dpi=1000)
plt.show()