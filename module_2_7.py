

def get_multiplied_digits(number):

    str_number = str(number)

    first = int(str_number[0])


    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
        first = int(str_number[0:])


result = get_multiplied_digits(303045)  #при преобразовании строки(str) в число(int) нули убираются. все кроме того , что стоит в конце строки. нужно писать дополнительный блок для удаления этого нуля.
print(result)









