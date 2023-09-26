def half_div_met(fun, a, b, eps=0.0001):
    if a > b:
        a, b = b, a
    if a == b:
        if fun(a) == 0:
            return f"{a} - корень"
        else:
            return f"{a} - не корень"

    fl = fun(a)
    fr = fun(b)

    if fl * fr > 0:
        print('Функція на краях відрізка [A,B] повинна мати різні знаки.')
        return None

    while b - a > eps:
        x = (a + b) / 2
        f = fun(x)
        if fl * f < 0:
            b = x
            fr = fun(b)
        elif fr * f < 0:
            a = x
            fl = fun(x)
        else:  # якщо точно потрапили в корінь
            x = (a + b) / 2
            return x
    return x


def list_to_file(list_data, filename):
    result = tuple(zip(list_data[::2], list_data[1::2]))
    with open(filename, 'w') as output_file:
        output_file.write("Data: " + str(list_data) + '\n')
        output_file.write("Result: " + str(result))
