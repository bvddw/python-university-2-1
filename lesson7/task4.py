import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

nframes = 100  # кількість кадрів


def X(t):
    return np.e ** t * (np.cos(t) + np.sin(t))


def Y(t):
    return np.e ** t * (np.cos(t) - np.sin(t))


tmin = 0
tmax = 2 * np.pi
t = np.linspace(tmin, tmax, 100)
x = X(t)
y = Y(t)
xmin = np.floor(min(x))
xmax = np.floor(max(x)) + 1
ymin = np.floor(min(y))
ymax = np.floor(max(y)) + 1
fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.plot(x, y, lw=3, color='black')
pt, = ax.plot([X(tmin)], [Y(tmin)],  'ro', markersize=15)
ttl = ax.text((xmax + xmin) / 2, 1.1 * ymax, '')  # текстовий об'єкт


def animate(i):
    tp = tmin + i * (tmax - tmin) / nframes  # момент часу по номеру кадра i
    xp = X(tp)
    yp = Y(tp)
    ttl.set_text('t={:4.2f}'.format(tp))
    pt.set_data(xp, yp)
    return pt, ttl


anim = FuncAnimation(fig, animate, frames=nframes,
                     interval=50)
anim.save("task4.gif", writer='pillow')
