def reversed_digits(number: int):
    if number < 10:
        print(number)
        return
    print(number % 10)
    return reversed_digits(number // 10)


input_number = int(input('Enter number: '))
reversed_digits(input_number)