import math
import cmath


def func_1_4(x):
    return 6 * ((6 * (x - 3) ** 2) ** (1 / 3)) / (x ** 2 - 2 * x + 9)


def func_1_5(x):
    y = (math.cos(math.log(7)) * (cmath.sin(7 * x) ** 2)) / (7 * cmath.cos(14 * x))
    return complex(round(y.real, 4), round(y.imag, 4))


def func_1_6(x):
    return 2 * math.log(x) + x ** 2 - 4 * x + 3


def f1(x):
    a = 6 * math.pow(6 * (x - 2) ** 2, 1 / 3)
    b = (x ** 2 - 2 * x + 9)
    return a / b


def f2(x):
    return 2 * math.log(x) + x ** 2 - x * x + 3


def f3(x):
    return (f1(x) + f2(x)) / 2


def f(x, a=1, b=5):
    if x < a:
        return f1(x) - f1(a)
    elif a <= x <= b:
        return f2(x) - f2(a)
    else:
        return f3(x) - f3(b) + f2(b) - f2(a)


def func_2_2(xl=-1, xr=7):
    for i in range(10):
        x = xl + (xr - xl) * i / 9
        print('\t', round(x, 4), '\t', round(f(x), 4))


def func_2_7(x):
    return 4 / (x + math.sqrt(x * x + x)) - (1 / (x - math.sqrt(x * x + x))) - 3 / x