import math


def elem(n):
    return n / math.pow(2, n)


alph = 0.1
n = 1
sgn = -1
a = sgn * elem(n)
s = 0.0
while abs(a) > alph:
    s += a
    n +=1
    sgn = -sgn
    a = sgn * elem(n)
print(f'Suma = {round(s, 2)}')