
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers


    def is_valid_vin(self):

        if isinstance(self.__vin, int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера'")
        else:
            self.is_valid_number()

    def is_valid_number(self):

        if isinstance(self.__numbers, str) == False:
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        if len(self.__numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message



try:
    first = Car('Model1', 1000000, 'f123dj')
    Car.is_valid_vin(first)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)#
else:
    print(f'{first.model} успешно создан')


try:
  second = Car('Model2', 300, 'т001тр')
  Car.is_valid_vin(second)
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
  Car.is_valid_vin(third)
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')