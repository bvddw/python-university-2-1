from random import randint

left = 0
right = 100
numbers = [randint(left, right) for i in range(20)]
print(numbers)
a = int(input("Enter number: "))
suma = sum(filter(lambda item: item < a, numbers))
print(f"Suma of items, that less than a ({a}): {suma}")