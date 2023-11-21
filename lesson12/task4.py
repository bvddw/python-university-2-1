import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.misc import derivative


# Задане рівняння функції
def original_function(x):
    return 6 * (6 * (x - 3) ** 2) ** (1 / 3) / (x ** 2 - 2 * x + 9)


# Задані точки для інтерполяції
x_interpolation = np.linspace(1, 6, 6)
y_interpolation = original_function(x_interpolation)

# Побудова кубічних сплайнів з різними граничними умовами
cs_natural = CubicSpline(x_interpolation, y_interpolation, bc_type='natural')
cs_clamped = CubicSpline(x_interpolation, y_interpolation, bc_type='clamped', extrapolate=False)
cs_deriv1 = CubicSpline(x_interpolation, y_interpolation, bc_type=((1, derivative(original_function, 1, dx=0.1, n=1)),
                                                                   (1, derivative(original_function, 6, dx=0.1, n=1))))
cs_deriv2 = CubicSpline(x_interpolation, y_interpolation, bc_type=((2, derivative(original_function, 1, dx=0.1, n=2)),
                                                                   (2, derivative(original_function, 6, dx=0.1, n=2))))

# Визначення нових точок для відображення графіків
x_plot = np.linspace(1, 6, 1000)
y_original = original_function(x_plot)
y_natural = cs_natural(x_plot)
y_clamped = cs_clamped(x_plot)
y_deriv1 = cs_deriv1(x_plot)
y_deriv2 = cs_deriv2(x_plot)

# Побудова графіків
plt.figure(figsize=(12, 8))

# Графік функції та інтерполяційних точок
plt.subplot(2, 2, 1)
plt.plot(x_plot, y_original, label='Функція')
plt.scatter(x_interpolation, y_interpolation, color='red', label='Інтерполяційні точки')
plt.title('Функція та інтерполяційні точки')
plt.legend()

# Графік кубічного сплайну з природніми граничними умовами
plt.subplot(2, 2, 2)
plt.plot(x_plot, y_original, label='Функція')
plt.plot(x_plot, y_natural, label='Природні границі')
plt.scatter(x_interpolation, y_interpolation, color='red', label='Інтерполяційні точки')
plt.title('Природні границі')
plt.legend()

# Графік кубічного сплайну з затисненими граничними умовами
plt.subplot(2, 2, 3)
plt.plot(x_plot, y_original, label='Функція')
plt.plot(x_plot, y_clamped, label='Затиснені границі')
plt.scatter(x_interpolation, y_interpolation, color='red', label='Інтерполяційні точки')
plt.title('Затиснені границі')
plt.legend()

# Графік кубічного сплайну з границями похідних
plt.subplot(2, 2, 4)
plt.plot(x_plot, y_original, label='Функція')
plt.plot(x_plot, y_deriv1, label='Задані похідні 1-го порядку')
plt.plot(x_plot, y_deriv2, label='Задані похідні 2-го порядку')
plt.scatter(x_interpolation, y_interpolation, color='red', label='Інтерполяційні точки')
plt.title('Границі похідних')
plt.legend()

# Показати графіки
plt.tight_layout()
plt.show()
