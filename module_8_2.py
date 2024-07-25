

def personal_sum(*numbers):
    count = 0
    result = 0
    incorrect_data = 0
    print('\n', *numbers)

    for i in numbers:  # обход скобок, чтобы добраться до данных
        for j in i:
            try:       # прогноз на не соответствие требованию коллекции
                for num in j:
                    try:     # прогноз на не соответствие требованию числительному
                        result += num
                        count += 1

                    except TypeError as exc:
                        incorrect_data += 1
                        print(f'Некорректыный тип данных {num} ')
            except TypeError as exc:
                print('Передана не коллекция')
                return None

    return (result, count, incorrect_data)

def calculate_average(*numbers):

    avg1 = personal_sum(numbers)
    try:            # прогноз на не соответствие операций с нулем и коллекции
        avg = avg1[0] / avg1[1]
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None
    return avg

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

