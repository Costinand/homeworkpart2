import time
import asyncio

async def start_strongman(name, power):
    number = 1

    print(f'Силач {name} начал соревнования.')
    while number < 6:
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {number} - й шар')
        number += 1
    print(f'\33[31m Силач  {name} завершил соревнование \033[0m')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Григорий', 4))  # запуск задания
    task2 = asyncio.create_task(start_strongman('Василий', 5))
    task3 = asyncio.create_task(start_strongman('Иван', 3))
    await task1  # ожидание исполнения задания
    await task2
    await task3

asyncio.run(start_tournament())