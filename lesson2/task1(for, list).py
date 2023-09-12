import math


x_values = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
print('Using for ... in list')
print('x', '\t\t y', '\t\t y**2', '\texp(-y)')
print('-' * 32)
for x in x_values:
    y = 2 * math.log(x) + x ** 2 - 4 * x + 3
    print(round(x, 2), '\t', round(y, 3), '\t', round(y ** 2, 3), '\t', round(math.exp(-y), 3))