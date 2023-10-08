import numpy as np

n = int(input('n = '))
arr = np.round(20 * (0.5 - np.random.random(n)), 2)
max_index = np.argmax(arr)
min_index = np.argmin(arr)
print(f"Original array: {arr}")
first_part = arr[1::2].copy()
second_part = arr[::2].copy()
arr[:n // 2] = first_part
arr[n // 2:] = second_part
print(f"New array: {arr}")
print(f"Index of max item: {max_index}")
print(f"Index of min item: {min_index}")
