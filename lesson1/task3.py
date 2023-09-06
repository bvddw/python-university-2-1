import math

# Task 3
print('task 3:')
a = float(input('\tEnter a: '))
x = float(input('\tEnter x: '))
sqrt = math.sqrt(x ** 2 + a)
result = sqrt + x ** 2 / sqrt + a * (1 + x / sqrt) / (x + sqrt)
print(f'\ttask 3: {result}')
print(f'\texpected result for (1, -1): {2 * math.sqrt(2)}')
