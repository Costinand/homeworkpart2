import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

########### РАБОТА С ИЗОЮРАЖЕНИЕМ PIL ###########

with Image.open("cat.gif") as im: # открытие файла

    print(im.mode) # Тип цветности
    index = 1
    for frame in ImageSequence.Iterator(im): # разбитие ряда на кадры
        frame.save(f"frame{index}.png")
        index += 1

img1 = Image.open('frame1.png') # открытие кадров
img2 = Image.open('frame2.png')
img1 = img1.convert("RGB")  #  конвертация в RGB для дальнейшей работы
img2 = img2.convert("RGB")
img = Image.blend(img1, img2, 0.5) # соединение изображений с прозрачностью 0.5
img.show()

arr_1D = np.arange(1,13)

################ РАБОТА С МАССИВОМ NUMPY #######################
def arr_info():
    print(f'размерность массива {arr.ndim}') # размерность массива
    print(f'парметры размера {arr.shape}') # параметры (горизонталь и вертикаль)
    print(f'количество элементов {arr.size}')  # количество элементов
    print(arr)

arr = np.arange(1,13)
arr_info()
arr.shape = 3, 4 # изменение фигуры массива
arr_info()

arr[0, 0] = 3
arr_info()
arr[2, 3] -= 3


arr *= 2
arr_info()
arr[1: 2] -= 3
arr[2:3]  -= 7

arr.shape = 2, 6
arr_info()

############## РАБОТА С ГРАФИКОМ MATPLOTLIB ##########

for i in list(arr):
    plt.plot([d for d in range(6)], i)
    plt.plot([d for d in range(6)], i)
    plt.xlabel("Рабочие дни")
    plt.ylabel("Загрузка оборудования -- Эффективность")
    plt.title("Пиковые нагрузки и норма выработки")
    plt.axis('on')
plt.show()
