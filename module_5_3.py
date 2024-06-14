class Building:

    def __init__(self, number, Type):

        self.numberOfFloors = number
        self.buildingType = Type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

tower = Building(15, "brics")
castle = Building(6, "stone")

print(tower == castle)



