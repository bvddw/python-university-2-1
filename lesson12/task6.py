import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Параметричне рівняння кривої
def parametric_curve(t):
    x = 3 * (t - np.sin(t))
    y = 3 * (1 - np.cos(t))
    return x, y

# Генеруємо значення параметра t в заданому діапазоні
t_values = np.linspace(0, 2*np.pi, 1000)

# Отримуємо координати кривої для всього діапазону
x_curve, y_curve = parametric_curve(t_values)

# Обираємо 7 точок
selected_points_indices = np.linspace(0, len(t_values)-1, 7, dtype=int)
x_selected = x_curve[selected_points_indices]
y_selected = y_curve[selected_points_indices]

# Закриваємо криву, щоб остання точка була тією ж, що й перша
x_selected = np.append(x_selected, x_selected[0])
y_selected = np.append(y_selected, y_selected[0])

# Будуємо інтерполяційний кубічний сплайн з періодичними граничними умовами
t_interp = np.arange(len(x_selected))
cs = CubicSpline(t_interp, np.column_stack((x_selected, y_selected)), bc_type='periodic')

# Генеруємо значення для плавного графіку сплайну
t_spline = np.linspace(0, len(x_selected)-1, 1000)
x_spline, y_spline = cs(t_spline).T  # Transpose to get separate x and y arrays

# Малюємо графік
plt.figure(figsize=(10, 6))
plt.scatter(x_selected, y_selected, label='Інтерполяційні точки', color='red')
plt.plot(x_curve, y_curve, label='Параметрична крива', linestyle='dashed', color='blue')
plt.plot(x_spline, y_spline, label='Інтерполяційний кубічний сплайн', linestyle='dashed', color='green')
plt.title('Інтерполяційний кубічний сплайн з періодичними граничними умовами')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# Генеруємо значення параметра t в заданому діапазоні
t_values = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Обчислюємо відповідні значення x та y для кожного t
x_values, y_values = parametric_curve(t_values)

# Малюємо графік
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, label='Parametric Curve')
plt.title('Parametric Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()