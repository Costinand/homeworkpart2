class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if  food.edible:
            print(self.name, "съел", food.name)
            self.fed = True
        else:
            print(self.name, "не стал есть", food.name)
            self.alive = False


class Plant:

    def __init__(self, name):
        self.name = name
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name

class Flower(Plant):
    pass

class Predator(Animal):
    pass

class Mammal(Animal):
    pass

a1 = Predator("Волк")
a2 = Mammal("Овца")
p1 = Flower("Ромашка")
p2 = Fruit('Апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)




