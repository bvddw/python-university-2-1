from random import randint
n = 10
l = [randint(0, 4) * 2 + 1 for i in range(n)]
print('List:', l)
tuple1 = l[::2]
tuple2 = l[1::2]
result = tuple(zip(tuple1, tuple2))
print('Tuple of tuples:', result)
