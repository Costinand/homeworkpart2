class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number



    def go_to(self, new_floor):
        n = new_floor
        print(self.name)
        if n > self.number_of_floors or n < 1:
            print("Такого этажа не существует")
        else:
            for i in range(n):
                print(i + 1)


h1 = House("Air", 18)
h1.go_to(12)
h2 = House("Синички", 8)
h2.go_to(10)


