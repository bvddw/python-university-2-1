from random import randint

left = 0
right = 100
numbers = [randint(left, right) for i in range(20)]
print(numbers)
a = int(input("Enter number: "))
suma = 0
count = 0
for item in numbers:
    if item < a:
        suma += item
        count += 1
print(f"Suma of items, that less than a ({a}): {suma}, amount: {count}")