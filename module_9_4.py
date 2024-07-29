import random
from pprint import pprint


first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)



def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{str(data)}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        x = random.choice(self.words)
        return x


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Возможно')

print(first_ball())
print(first_ball())
print(first_ball())




