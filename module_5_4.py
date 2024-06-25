class Buiilding:
    total = 0

    def __init__(self):
        Buiilding.total += 1

for i in range(40):
    obj = Buiilding()
    print(obj)
print(Buiilding.total)


