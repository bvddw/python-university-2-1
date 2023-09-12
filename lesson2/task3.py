import math

s = 0
for n in range(1, 11):
    s += math.atan(5 / n) / math.factorial(n)
print(f'Сума перших 10 членів = {s}')