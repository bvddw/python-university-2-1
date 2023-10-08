import numpy as np

x = np.array([-4, 2, 1])
A = np.array([[2, 1, 0], [3, 0, 4], [1, -1, 2]])
B = np.array([[0, 2, 3], [4, 1, 0], [2, -1, -2]])

y = (A.dot(A) + B.dot(B)).dot(x)
print('(A^2+B^2).x=', y)

z = (A.dot(B) - B.dot(A)).dot(x)
print('(A.B-B.A).a=', z)

u = np.linalg.inv(A).dot(x)
print('A^(-1).x=', u)

print('max(B)=', B.max())
