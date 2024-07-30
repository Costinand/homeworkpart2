import threading
from time import sleep
from datetime import datetime

time_start = datetime.now()

def write_words(word_count, file_name):

    with open(file_name, 'a', encoding='utf-8') as file:

        for i in range((word_count)):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


result1 = write_words(10, 'example1.txt')
result2 = write_words(30, 'example2.txt')
result3 = write_words(200, 'example3.txt')
result4 = write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа одного потока: {time_res}')


time_start = datetime.now()

thr1 = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thr2 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thr3 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thr4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

time_end = datetime.now()
time_res = time_end - time_start

print(f'Работа потоков: {time_res}')