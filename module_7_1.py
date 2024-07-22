from pprint import pprint
import os

#импорт модулей для работы с файлом


class Shop():
    content = [] # список созается на основе файла


    def __init__(self, file_name = 'products.txt'):
        self.__file_name = file_name
        # конструктор магазина

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read() # запись содержимого файла для оперции с ним


    def add(self, *products): #в этом методе кандидаты на добавления будут проверяся на наличие. звездочка говорит о
        # любом объеме списка

        with open(self.__file_name, 'r+') as file:
            if os.stat("products.txt").st_size == 0: #проверка что файл пуст
                # print('Пустой ')
                names = [] #список из наименований

                for i in products:  #перебор добавляемых продуктов
                    if i.name in names:  #если имя объекта есть в списке наименований
                        # print(i.name)
                        print('\033[36m',f'Продукт {i.name} уже есть в магазине','\033[0m')
                    else:
                        # print(i)
                        file.write(f'{i}\n') #иначе добавляем в файл объект
                        names.append(i.name)  # добавляем его имя в список наименований
                        # print(names)


                # file.close()


            else: # файл оказался не пустым
                # print("XXXXX")
                with open(self.__file_name, 'r+') as file:

                    
                    content = self.get_products() # заполнение списка содержимого магазмна


                    for j in products:  # перебор кандидатов
                        if j.name in content: #если имя кондидата есть списке из магазина
                            # print('aaasss')
                            print('\033[36m',f'Продукт {j} уже есть в магазине','\033[0m')

                    # print(file.read())




class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)


print(s1.get_products())
# pprint(file())

# print(dir(p2))

# print(vars(p2).values())

# for i in vars().values():
#     print(i)

# first_char = file_obj.read(1)
#
# if not first_char:
#     print("File is empty")
# else:
#     print("File is NOT empty")

