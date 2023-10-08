import numpy as np

n = 5
arr = np.random.randint(-9, 10, n * n)

matrix = arr.reshape(n, n)
print(f"Created matrix:\n{matrix}")

diag_indexes = np.arange(9)
diag_indexes -= 4

max_diagonals = [np.max(matrix.diagonal(-4)), np.max(matrix.diagonal(-3)), np.max(matrix.diagonal(-2)),
                 np.max(matrix.diagonal(-1)), np.max(matrix.diagonal(0)), np.max(matrix.diagonal(1)),
                 np.max(matrix.diagonal(2)), np.max(matrix.diagonal(3)), np.max(matrix.diagonal(4))]

print(f"Max of diagonals parallel to the main one:\n {max_diagonals}")

max_row_index = (24 - np.argmax(arr[::-1])) // 5
min_row_index = np.argmin(arr) // 5
print(f"Max element in row: {max_row_index}")
print(f"Min element in row: {min_row_index}")
row_with_max_elem = arr[max_row_index * 5: max_row_index * 5 + 5].copy()
row_with_min_elem = arr[min_row_index * 5: min_row_index * 5 + 5].copy()
arr[max_row_index * 5: max_row_index * 5 + 5] = row_with_min_elem
arr[min_row_index * 5: min_row_index * 5 + 5] = row_with_max_elem
print(f"New matrix:\n{matrix}")