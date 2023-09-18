n = int(input('n = '))
last_digit = n % 10
n_wo_last = n // 10
number_of_digits = int(input('How many digits do you want to add?\n'))
for i in range(number_of_digits):
    digit = int(input('Enter digit: '))
    n_wo_last = n_wo_last * 10 + digit
n_wo_last = n_wo_last * 10 + last_digit
print(f'Old n: {n}')
print(f'New n: {n_wo_last}')
