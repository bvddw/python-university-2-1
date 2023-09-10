import math
import turtle
from turtle import *

reset()

kx = 50
ky = 500

color('red')
width(2)
maxy = 0.5
up()
goto(-kx * 2 * math.pi, 0)
down()
goto(kx * 2 * math.pi, 0)
up()
goto(0, ky * maxy)
down()
goto(0, - ky * maxy)

color('blue')
width(3)

x = math.pi / 25
y = 2 * math.log(x) + x ** 2 - 4 * x + 3
dx = math.pi / 25
up()
goto(kx * x, ky * y)
down()

for i in range(100):
    y = 2 * math.log(x) + x ** 2 - 4 * x + 3
    goto(kx * x, ky * y)
    x += dx

turtle.mainloop()