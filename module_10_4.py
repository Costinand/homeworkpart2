from threading import Thread
from time import sleep
from queue import Queue
from random import randint

queue = Queue()

class Table():
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest
        self.name_guest = ' '


class Guest(Thread):
    def __init__(self, *name):
        super().__init__()
        self.name = name

    def run(self, guest):
        s = randint(3, 10)
        sleep(s)
        Table.guest = None


class Cafe():
    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for g in guests_names:
            customer = Guest(g)
            if all(table.guest is True for table in tables):
                print(f'{g} - ожидает')
                table.name_wait = g
                queue.put(customer)
            else:
                for table in tables:
                    if table.guest == None:
                        print(f' {g} сел(-а) за стол номер {table.number}')
                        table.guest = True
                        table.name = g
                        c_a = Thread(target=Guest.run, args=(table.number, g))
                        c_a.start()
                        c_a.join()
                        break


    def discuss_guests(self, c_a):
        while not queue.empty() or any([table.guest for table in tables]):
            for table in tables:

                if table.guest is not None and not c_a.is_alive():
                    print(f'{table.name} покушал(-а) и ушёл(-ла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None#
                if not queue.empty() and table.guest is None:
                    table.guest = queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.name = table.guest.name
                    c_d = Thread(target=Guest.run, args=(table.number, table.guest.name))
                    c_d.start()
                    c_d.join()

tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)

guests_names = ['Maria', 'Oleg', 'Vasiliy', 'Sergey', 'Darya', 'Andrey','Vitoria', 'Nikita', 'Galina', 'Pavel',
                'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]
c_a = Thread(target=Guest.run)
cafe.guest_arrival(*guests)
cafe.discuss_guests(c_a)




# guests_names = ['1-Maria', '2-Oleg', '3-Vasiliy', '4-Sergey', '5-Darya', '6-Andrey','7-Vitoria', '8-Nikita', '9-Galina', '10-Pavel',
#                 '11-Ilya', '12-Alexandra']



