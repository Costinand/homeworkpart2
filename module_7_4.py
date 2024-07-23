import random
# number = []
# score = []
# time = []

class Game_teams():

    def __init__(self, *name):
        self.name = name




    def start(self, *teams):
        for team in teams:

            self.number = int(random.uniform(5, 8))
            print(self.number)

            print(f'{team}',)

        return self.number

class Teams():
    def __init__(self, name, number, score, time):
        self.name = name
        self.number = number
        self.score = score
        self.time = time

    def __str__(self):
        return f'{self.name}, {self.number}, {self.score}, {self.time}'

    def get_team(self):
        return self.number



t1 = Teams("Мастера кода", 0, 0, 0)
t2 = Teams("Волшебники данных",0, 0, 0
           )

summer_cup2024 = Game_teams()
summer_cup2024.start(t1, t2)

print(t1.get_team())
print(t2.get_team())


# add_team(t1, t2)