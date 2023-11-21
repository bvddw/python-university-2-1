import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_func(x, m, b):
    return m * x + b


def linear_approximation(x_values, y_values):
    # Використовуємо curve_fit для знаходження параметрів m та b
    params, covariance = curve_fit(linear_func, x_values, y_values)

    # Розпаковуємо параметри
    m, b = params

    # Виведення рівняння прямої
    print(f'Рівняння прямої: y = {m:.4f}x + {b:.4f}')

    # Зобразимо точки та апроксимаційну пряму
    plt.scatter(x_values, y_values, color='red', label='Точки')
    plt.plot(x_values, linear_func(np.array(x_values), m, b), color='blue', label='Апроксимаційна пряма')
    plt.title('Лінійна апроксимація')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


# Задані точки
points_3 = [(0, 2), (1, -2), (2, 1), (3, 2), (4, -1), (5, 0)]

# Розпаковка координат точок
x_values_3, y_values_3 = zip(*points_3)

# Виклик функції лінійної апроксимації та побудова графіків
linear_approximation(x_values_3, y_values_3)
