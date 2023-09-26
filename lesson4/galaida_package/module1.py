import math

# const from task 1
task_1_const = (((95 + 7 / 30) - (93 + 5 / 18)) * (2 + 1 / 4) + 0.373) / 0.2

# const from task 2
task_2_const = (math.cos(math.log(7)) * (math.sin(7 * math.sqrt(2)) ** 2)) / (7 * math.cos(14 * (math.e ** 2)))


def task_3_func(a, x):
    sqrt = math.sqrt(x ** 2 + a)
    result = sqrt + x ** 2 / sqrt + a * (1 + x / sqrt) / (x + sqrt)
    return result


def task_4_func(number: int):
    if number < 10:
        print(number)
        return
    print(number % 10)
    return task_4_func(number // 10)
