

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'metalic', 'red', 'oramge', 'green', 'brown', 'black', 'white']
    def __init__(self, owner, model, power, color):

        self.owner = owner
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def get_model(self):
        return model
    def get_horsepower(self):
        return power
    def set_color(self, new_color):

        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            self.__color = new_color

        else:
            print('\033[31m', "Нельзя сменить цвет на ",  new_color, '\033[0m')


    def print_info(self):
        print("Модель: ", self.__model)
        print("Мощность двигателя:", self.__engine_power )
        print("Цвет: ", self.__color)
        print("Владелец: ", self.owner)




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()


