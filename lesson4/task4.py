from math import sqrt
import sys


def f(x):
    y1 = 4 / (x + sqrt(x ** 2 + x)) - 1 / (x - sqrt(x ** 2 + x))
    y2 = 3 / x
    return y1 - y2


def half_div_met(fun, a, b, eps=0.0001):
    if a > b:
        a, b = b, a
    if a == b:
        if fun(a) == 0:
            return f"{a} - корень"
        else:
            return f"{a} - не корень"

    fl = fun(a)
    fr = fun(b)

    if fl * fr > 0:
        print('Функція на краях відрізка [A,B] повинна мати різні знаки.')
        return None

    while b - a > eps:
        x = (a + b) / 2
        f = fun(x)
        if fl * f < 0:
            b = x
            fr = fun(b)
        elif fr * f < 0:
            a = x
            fl = fun(x)
        else:  # якщо точно потрапили в корінь
            x = (a + b) / 2
            return x
    return x


# пошук кореня функції F(x)
a = float(input('A = '))
b = float(input('B = '))
eps = 0.00001  # похибка обчислення кореня
dig = len(str(int(1 / eps)))
root = half_div_met(f, a, b, eps)
if root is None:
    print("Розв'язок не знайдено.")
    sys.exit()
print('x2 =', round(root, dig))
