import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify

def lagrange_interpolation(x_values, y_values, x):
    result = 0
    for k in range(len(y_values)):
        term = y_values[k]
        for i in range(len(x_values)):
            if i != k:
                term *= (x - x_values[i]) / (x_values[k] - x_values[i])
        result += term
    return result

def lagrange_polynomial(x_values, y_values):
    x = symbols('x')
    polynomial = 0
    for k in range(len(y_values)):
        term = y_values[k]
        for i in range(len(x_values)):
            if i != k:
                term *= (x - x_values[i]) / (x_values[k] - x_values[i])
        polynomial += term
    return simplify(polynomial)

def plot_interpolation(x_values, y_values, title):
    x_interpolation = np.linspace(min(x_values), max(x_values), 1000)
    y_interpolation = [lagrange_interpolation(x_values, y_values, x) for x in x_interpolation]

    polynomial = lagrange_polynomial(x_values, y_values)
    print(f'Інтерполяційний многочлен для {title}:')
    print(polynomial)

    plt.figure()
    plt.scatter(x_values, y_values, color='red', label='Точки')
    plt.plot(x_values, y_values, linestyle='dashed', color='blue', label='Ламана')
    plt.plot(x_interpolation, y_interpolation, color='green', label='Інтерполяційний поліном')
    plt.title(title)
    plt.legend()
    plt.show()

# Задані точки
points_3 = [(1, 3), (2, 2), (3, 4), (4, 6), (5, 2)]

# Побудова графіків
plot_interpolation(*zip(*points_3), title='Набір точок 3')