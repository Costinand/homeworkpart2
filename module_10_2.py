from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        sleep(1)
        d = 0
        n = 100
        while n > 0:
            n -= self.power
            d += 1
            print(f'{self.name} сражается {n}, осталось {n} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {d} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

