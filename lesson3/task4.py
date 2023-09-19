def sum_of_iter(iter_obj):
    suma = 0
    for item in iter_obj:
        if isinstance(item, int) or isinstance(item, float):
            suma += item
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            suma += sum_of_iter(item)
    return suma


def sum_of_dict_with_including(new_dict):
    suma = 0
    for key, value in new_dict.items():
        if isinstance(key, int) or isinstance(key, float):
            suma += key
        elif isinstance(key, tuple) or isinstance(key, set):
            suma += sum_of_iter(key)
        elif isinstance(key, dict):
            suma += sum_of_dict_with_including(key)
        if isinstance(value, int) or isinstance(value, float):
            suma += value
        elif isinstance(value, list) or isinstance(value, tuple) or isinstance(key, set):
            suma += sum_of_iter(value)
        elif isinstance(value, dict):
            suma += sum_of_dict_with_including(value)
    return suma


def sum_of_dict_wo_including(new_dict):
    suma = 0
    for key, value in new_dict.items():
        if isinstance(key, int) or isinstance(key, float):
            suma += key
        if isinstance(value, int) or isinstance(value, float):
            suma += value
    return suma


my_dict = {
    1: 1,
    2: 2,
    3: [1, 2, 3, {}],
}
print(sum_of_dict_wo_including(my_dict))