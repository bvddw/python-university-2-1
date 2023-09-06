import math

# Task 4
print('task 4:')
for x in range(5):
    y = 6 * ((6 * (x - 3) ** 2) ** (1 / 3)) / (x ** 2 - 2 * x + 9)
    print(f'\tx = {x}: y = {round(y, 4)}')
