import os
import datetime
from threading import Thread
import multiprocessing

all_data = []


def read_info(name):
    with open(name, 'r+', encoding='utf-8') as file:
        line = file.readline()
        while line:
            line = line.rstrip('\n')
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]



# ПОТОКОВОЕ ИСПОЛНЕНИЕ
threads = []
for name in filenames:
    thr = Thread(target=read_info, args=(name, ))
    thr.start()
    threads.append(thr)
    start = datetime.datetime.now()

for thr in threads:
    thr.join()

end = datetime.datetime.now()
print(end - start)


# МУЛЬТИПРОЦЕССОРНОЕ ИСПОЛНЕНИЕ
# if __name__ == '__main__':
#     with multiprocessing.Pool(processes = 4) as pool:
#         start = datetime.datetime.now()
#         pool.map(read_info, filenames)
#     end = datetime.datetime.now()
#     print(end - start)




