import random
team1 = "Мастера кода"
team2 = "Волшебники данных"
number = []
score = []
time = []

for i in range(2):
    num = int(random.uniform(5, 7))
    scr = int(random.uniform(39, 42))
    tm = round(random.uniform(13000,18000) , 1) # ограничение точности ло одного знака

    number.append(num)
    score.append(scr)
    time.append(tm)

def challeng_result():
    sc_1 = score[0]
    sc_2 = score[1]
    team1_time = time[0]
    team2_time = time[1]
    if sc_1 > sc_2 or sc_1 == sc_2 and team2_time > team1_time:
        result = f'Победа команды {team1}!'
    elif sc_1 < sc_2 or sc_1 == sc_2 and team2_time < team1_time:
        result = f'Победа команды {team2}!'
    else:
        result = 'Ничья!'
    return result

task_total = sum(score)
time_avg = round(sum(time) / task_total, 1)

print('В команде %s' % 'Мастера кода участников: %s' % number[0] )
print('В команде %s, участников: %s' % ('Волшебники данных', number[1]))
print('Итого сегодня в командах участников: %s' % number[0], 'и %s'% number[1])

print('\nКоманда {} решила задач: {}'.format(team2, score[1]),'!')
print('Команда {} решила задач: {}'.format(team1, score[0]),'!')

print('{} решили задачи за {}'.format(team2, time[1]), 'с !')
print('{} решили задачи за {}'.format(team1, time[0]), 'с !')
print(f'\nКоманды решили {score[0]} и {score[1]} задач')
print(challeng_result())
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!.')

# ДЛЯ ПРОВЕРКИ РАБОТЫ СУДЬИ
# print(" M B ")
# print(number)
# print(score)
# print(time)
