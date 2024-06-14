class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors


        print(floors)

set_Num = House(12)
set_Num.setNewNumberOfFloors(15)