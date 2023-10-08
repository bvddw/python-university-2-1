import numpy as np

A = np.array([[1, 3, 0], [2, 1, -1], [0, 2, 1]])
B = np.array([[2, 1, 2], [3, 0, 2], [1, 0, 1]])
M = 2 * A.dot(A) + 3 * A + 5 * np.eye(3)
print('M=\n', M)

A1 = np.linalg.inv(A)
print('Обернена A=\n', A1)

dt = np.linalg.det(A)
print('Визначник=', dt)

print('A+B=\n', A + B)
print('A-B=\n', A - B)
print('A.B=\n', A.dot(B))
print('A*B=\n', A * B)
print('A.B-A*B=\n', A.dot(B) - A * B)
X = A1.dot(B)
print('X=\n', np.around(X, 4))
