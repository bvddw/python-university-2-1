from random import randint

n = 10
l = [randint(0, 4) * 2 + 1 for i in range(n)]

tuple1 = l[::2]
tuple2 = l[1::2]
result = tuple(zip(tuple1, tuple2))
with open('task1.txt', 'w') as output_file:
    output_file.write('List: ' + str(l) + '\n')
    output_file.write('Tuple of pairs: ' + str(result))

