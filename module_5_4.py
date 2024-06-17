total_str = []

class Building:

    def __init__(self, total):

        for i in range(total):
            total_str.append("Home_" + str(i + 1))

new_luzhki = Building(40)

print(total_str)



