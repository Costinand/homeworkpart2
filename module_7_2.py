from pprint import pprint

file_name = "test.txt"
string_position = {} # создание словаря


def custom_write(file_name, strings):
    with open(file_name, 'r+', encoding='utf-8' ) as file:
        n = 0
        for i in strings: # перебор строк будующего файла

            n += 1 # содание номера строки
            string_position[n, file.tell()] = i # создание елемента словаря. запрос положения начала
            # строки(позиция курсора) до записи в файл, иначе курсор окажется в конце строки в файле
            file.write(f'{i}\n') #  запись строки в файл


        return string_position  #  по окончании цикла перебора возврат системе готового словаря



info = ['Text for tell.',
        'Используйте кодировку utf-8.'
    ,'Because there are 2 languages!','Спасибо!']  # список для создания файла
result = custom_write('test.txt', info)  #  вызов создания файла

for elem in result.items(): # цикл для вывода словаря в удобном виде виде отдельных элементов словаря при помощи item
  print(elem)



