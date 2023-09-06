import math
import cmath

# Task 5
print('task 5:')
xr = float(input('\tEnter real part of x: '))
xi = float(input('\tEnter img part of x: '))
x = complex(xr, xi)
# x = complex(input())
print(f'\tYour complex number: {x}')
y = (math.cos(math.log(7)) * (cmath.sin(7 * x) ** 2)) / (7 * cmath.cos(14 * x))
yr = complex(round(y.real, 4), round(y.imag, 4))
print(f'\tround y = {yr}')
print(f'\tx + y = {x + yr}')
print(f'\tx * y = {x * y}')
print(f'\tx / y = {x / y}')
