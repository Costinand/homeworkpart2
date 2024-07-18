class Vehicle:
    __COLOR_VARIANTS = ['blue', 'metalic', 'red', 'oramge', 'green', 'brown', 'black', 'white']
    def __init__(self, owner, model, power, color):

        self.owner = owner
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def get_model(self):
        print("\nМодель: ", self.__model)
        return self.__model

    def get_horsepower(self):
        print("Мощность двигателя:", self.__engine_power)
        return self.__engine_power

    def set_color(self, new_color):

        print("\nпроверка наличия цвета в какталоге ", new_color)
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            print('\033[36m', 'Установка','\033[0m')
            self.__color = new_color

        else:
            print('\033[31m', "Нельзя сменить цвет на ",  new_color, '\033[0m')

    def get_color(self):
        print("Цвет: ", self.__color)
        return self.__color


    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print("Владелец: ", self.owner)




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()


