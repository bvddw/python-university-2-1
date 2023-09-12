import math


print('Using while (...)')
print('x', '\t\t y', '\t\t y**2', '\texp(-y)')
print('-' * 32)
x = 1.0
while x <= 2.0:
    y = 2 * math.log(x) + x ** 2 - 4 * x + 3
    print(round(x, 2), '\t', round(y, 3), '\t', round(y ** 2, 3), '\t', round(math.exp(-y), 3))
    x += 0.1