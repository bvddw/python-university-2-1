import math


def f(x: float):
    x1 = 4 / (x + math.sqrt(x * x + x))
    x2 = 1 / (x - math.sqrt(x * x + x))
    x3 = 3 / x
    return x1 - x2 - x3


a = float(input('A = '))
b = float(input('B = '))
eps = 0.000000000000000000000001
dig = len(str(int(1 / eps)))

if a >= b:
    print('А має бути менший за В.')
elif f(a) * f(b) > 0:
    print('Корінь має бути локалізований на відрізку [A, B].')
elif f(a) == 0:
    print(f'x = {a}')
elif f(b) == 0:
    print(f'x = {b}')
else:
    fl = f(a)
    fr = f(b)
    while b - a > eps:
        x = (a + b) / 2
        # print(a, x, b)
        fm = f(x)
        if fl * fm < 0:
            b = x
            fr = fm
        elif fr * fm < 0:
            a = x
            fl = fm
        else:
            print(f'x = {round(x, dig)}')
            break
