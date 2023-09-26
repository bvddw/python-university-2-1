import random

from galaida_package import module1, module2, module3


# first module testing
print(f"\nConst from task 1: {module1.task_1_const} == 23 + 173 / 200")
print(f"\nConst from task 2: {module1.task_2_const}")
print(f"\nFunc from task 3: {module1.task_3_func(1, -1)} == 2 * sqrt(2)")
print(f"\nFunc from task 4:")
module1.task_4_func(123456)


# second module testing
print(f"\nTask 1.4:")
for x in range(5):
    y = module2.func_1_4(x)
    print(f'\tx = {x}: y = {round(y, 4)}')

print(f"\nTask 1.5:")
x = complex(1, 2)
y = module2.func_1_5(x)
print(f'\tx = {x}')
print(f'\trounded y = {y}')
print(f'\tx + y = {x + y}')
print(f'\tx * y = {x * y}')
print(f'\tx / y = {x / y}')

print(f"\nTask 1.6:")
print(f"\tResult in x = 1: y = {module2.func_1_6(1)}")

print(f"\nTask 2.2:")
module2.func_2_2()

print(f"\nTask 2.7:")
print(f"\tResult in x = 0.5625: y = {module2.func_2_7(0.5625)}, because x = 0.5625 is a root.")


# third module testing
def f(x):
    return (x - 1) * (x - 3)


print(f"\nHalf division method: ")
print(f"\tRoot of function (x - 1) * (x - 3) on (0, 2) is: {module3.half_div_met(f, 0, 2, 0.0001)}")

filename = "task5.txt"
data = [random.randint(0, 4) * 2 + 1 for i in range(10)]
module3.list_to_file(data, filename)
print("\nResult of task with writing data to file could be checked in file 'task5.txt'")
