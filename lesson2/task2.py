import math


def f1(x):
    a = 6 * math.pow(6 * (x - 2) ** 2, 1 / 3)
    b = (x ** 2 - 2 * x + 9)
    return a / b


def f2(x):
    return 2 * math.log(x) + x ** 2 - x * x + 3


def f3(x):
    return (f1(x) + f2(x)) / 2


def f(x):
    if x < a:
        return f1(x) - f1(a)
    elif a <= x <= b:
        return f2(x) - f2(a)
    else:
        return f3(x) - f3(b) + f2(b) - f2(a)


a = 1
b = 5
xl = -1
xr = 7
for i in range(10):
    x = xl + (xr - xl) * i / 9
    print('\t', round(x, 4), '\t', round(f(x), 4))