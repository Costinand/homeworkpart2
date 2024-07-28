first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(zip[0]) - len(zip[1]) for zip in zip(first, second) if len(zip[0]) - len(zip[1]) != 0)
#  разница  длин элементов из разных спискров, исключая ноль, используя объединение
second_result = (len(first[i]) - len(second[i]) == 0 for i in range(len(first)))
# проверка равенства элементов из разных списковб не объединяя их

print(list(first_result))
print(list(second_result))

