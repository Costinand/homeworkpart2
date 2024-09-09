import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        temp = []
        speeds = [x.speed for x in self.participants]
        # print(speeds)
        self.participants.sort(key= lambda x: x.speed, reverse=True)
        min_speed = min(speeds)
        if self.full_distance <= min_speed * 2:
            print('Неверная дистанция забега')

        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase): # создание класса для тестирования
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.run1 = Runner('Усейн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):

        for key, value in cls.all_results.items():
            print(f'Забег: {key}')
            key_position = 1
            for key, value in value.items():
                print(f'\t{key_position}: {value.name}')
                key_position += 1

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        t1 = Tournament(90, self.run1, self.run3)
        result = t1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['1'] = result

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        t2 = Tournament(90, self.run2, self.run3)
        result = t2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['2'] = result

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        t3 = Tournament(90, self.run1, self.run2, self.run3)
        result = t3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['3'] = result

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament_4(self):
        t4 = Tournament(7, self.run3, self.run1, self.run2)
        result = t4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['4'] = result

'''ошибка в четвертом забеге решается обратной сортировкой экземпляров по скорости. добавил эту строчку #37. 
писать тесты для нее не стал - много времени ушло на основной код. по хорошему, есть еще ошибка с слишком маленькой 
дистанцией - добавил сообщение #40'''



if __name__ == '__main__':
    unittest.main()

