class Figure:
    filled = True
    sides_count = 1
    new_count = 1
    def __init__(self, color = (1, 1, 1), sides = [1]):
        self.__color = color
        color = (1, 1, 1)
        self._sides = sides


    def get_color(self):
        return self.__color

    def is_valid_color(self, new_color):
        summa = sum(new_color)
        if all(color >= 0 and color <= 255 for color in new_color) and isinstance(summa, int):
            setting()
            self.__color = new_color
        else:
            print('\033[31m', 'Неверные параметры цвета', '\033[0m')

    def set_color(self, color):
        print('\n', self.__class__.__name__, 'Проверка цвета')
        new_color = color
        print(new_color)
        self.is_valid_color(new_color)



    def get_sides(self):
        return self._sides


    def __is_valid_sides(self, new_sides):

        if self.new_count != self.sides_count:
            print('\033[31m', 'Неверное количество сторон', '\033[0m')
        else:
            self._sides = new_sides
            setting()


    def set_sides(self, sides):
        print('\n',self.__class__.__name__, 'Проверка сторон')
        new_sides = sides
        print(new_sides)
        new_count = len(new_sides)
        self.new_count = new_count
        self.__is_valid_sides(new_sides)



class Circle(Figure):
    def __init__(self, color, sides):
        super().__init__()
        sides_count = 1
        self.radius = sides

    def get_square(self):
        square = 3.14 * self.radius ** 2
        print('\nПлощадь круга ', square)

class Cube(Figure):
    def __init__(self, color, sides):
        super().__init__()
        self.sides_count = 12
        self._sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_volume(self):

        volume = self._sides[0] ** 3
        print('\nОбъем куба', volume)


class Triangle(Figure):
    def __init__(self, color, sides):
        super().__init__()
        self.sides_count = 3
        self._sides = [1, 1, 1]

    def get_square(self):
        p = sum(self._sides) / 2
        print(p)
        t = self._sides
        square1 = p * (p - t[0]) * (p - t[1]) * (p - t[2])
        square = square1 ** ( 1./ 2)
        print(t[1])
        print('\nПлощадь треугольника ', square)



def setting():
    print('\033[36m', 'Установка','\033[0m')

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    circle1.set_color((200, 200, 200))
    print(circle1.get_color())
    circle1.set_color((55, 66, 772))
    print(circle1.get_color())

    circle1.get_square()

    cube1 = Cube((222, 35, 130), 6)
    cube1.set_color((222, 35, 135))
    print(cube1.get_color())
    cube1.set_color((30.3, 70, 15))
    print(cube1.get_color())
    cube1.set_sides((5, 3, 12, 4, 5))
    print(cube1.get_sides())
    cube1.set_sides((6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6))
    print(cube1.get_sides())

    cube1.get_volume()

    triangle1 = Triangle((25, 165, 80), 5)
    triangle1.set_color((157, 29, 73))
    print(triangle1.get_color())
    triangle1.set_sides((2, 3, 4))
    print(triangle1.get_sides())

    triangle1.get_square()
