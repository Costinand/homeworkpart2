def print_params(a = 1, b = 'ff', c = True):
    print(a, b, c)

print_params()

# попытки вызвать функция с изменненным количеством аргументов не принесли результата.
# этот пункт задания не был с подвохом?
# вывести изменнное количество получилось лишь изменив вручную их значение на пустое место
print_params(a = '')
print_params(a = '', c = '' )
print_params(a = '', b = '', c = '')

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ('beta', 21, 17.5 )
values_dict = {'a': "tree", 'b': 13, 'c': 'border'}

print(*values_list)
print_params(**values_dict)

values_list_2 = (12, 'home')
print_params(*values_list_2, 42)