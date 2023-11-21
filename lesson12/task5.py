import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

def interpolate_lagrange(x_values, y_values, x):
    poly = lagrange(x_values, y_values)
    return poly(x)

def interpolate_cubic_spline(x_values, y_values, x):
    spline = CubicSpline(x_values, y_values, bc_type='clamped')
    return spline(x)

# Задані точки
points_3 = np.array([(0, 2), (1, -2), (2, 1), (3, 2), (4, -1)])

# Розпаковка координат точок
x_values_3, y_values_3 = points_3[:, 0], points_3[:, 1]

# Визначення нових точок для гладкої відображення графіків
x_plot = np.linspace(np.min(x_values_3), np.max(x_values_3), 1000)


# Графіки для третього набору точок
plt.figure(figsize=(15, 12))

# Розділення координат
x = points_3[:, 0]
y = points_3[:, 1]

# Побудова графіку інтерполяційної ламаної
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', label='Точки')
plt.plot(x, y, linestyle='dashed', label='Інтерполяційна ламана', color='blue')
plt.title('Інтерполяційна ламана (Набір 3)')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_plot, interpolate_lagrange(x_values_3, y_values_3, x_plot), color='green', label='Поліном Лагранжа')
plt.title('Інтерполяційний поліном Лагранжа (Набір 3)')
plt.legend()

plt.plot(x_plot, interpolate_cubic_spline(x_values_3, y_values_3, x_plot), color='orange', label='Кубічний сплайн')
plt.title('Інтерполяційний кубічний сплайн (Набір 3)')
plt.legend()

slope, intercept = np.polyfit(x_values_3, y_values_3, 1)
plt.plot(x_plot, slope * x_plot + intercept, color='purple', label='Апроксимуюча пряма')
plt.title('Апроксимуюча пряма (Набір 3)')
plt.legend()

# Показати графіки
plt.tight_layout()
plt.show()
