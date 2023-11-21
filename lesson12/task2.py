import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, sin, ln, diff

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

def plot_interpolation(x_values, y_values, func, title):
    x_interpolation = np.linspace(min(x_values), max(x_values), 1000)
    y_interpolation = [lagrange_interpolation(x_values, y_values, x) for x in x_interpolation]

    polynomial = lagrange_polynomial(x_values, y_values)
    print(f'Інтерполяційний многочлен для {title}:')
    print(polynomial)

    plt.figure()
    plt.plot(x_interpolation, y_interpolation, color='green', label='Інтерполяційний поліном')
    plt.plot(x_interpolation, [func(x) for x in x_interpolation], linestyle='dashed', color='blue', label='Вихідна функція')
    plt.scatter(x_values, [func(x) for x in x_values], color='red', label='Точки для інтерполяції')
    plt.title(title)
    plt.legend()
    plt.show()

# Задані функції та їх відрізки
func_1 = lambda x: sin(x) / (x**2 + 1)
func_2 = lambda x: ln(x**2 + 1) / (x**2 + 1)
func_3 = lambda x: sin(x) * np.cos(x**2 + 1) / (x**2 + 1)
func_4 = lambda x: sin(x) * ln(x**2 + 1) * 2**(-x)

interval_3 = np.linspace(-1, 1, 5)

# Побудова графіків
plot_interpolation(interval_3, [func_3(x) for x in interval_3], func_3, title='Функція 3')
