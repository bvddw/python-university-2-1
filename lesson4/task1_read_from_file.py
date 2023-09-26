with open("task1.txt", 'r') as input_file:
    data = ''
    list_result = []
    for row in input_file:
        data = row
    for i in data:
        try:
            list_result.append(int(i))
        except ValueError:
            continue
    print(list_result)