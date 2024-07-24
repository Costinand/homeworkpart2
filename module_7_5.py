import os
import time

for root, dirs, files in os.walk('.'): # осмотр всего , что текущем разделе и ниже
    for file in files:
        filepath = os.path
        filesize = os.path.getsize(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

print(os.path.join('\nsecond', 'Mother Goose - Monday’s Child.txt', 'fourth'))
