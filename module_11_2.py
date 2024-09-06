
import inspect

info = {} # словарь интроспекции

class Test():
    def __init__(self, value):
        self.object = object

def introspection_info(obj):

    info[type.__name__] = type(obj)  # добавленик в словарь info четырех параметров
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))] # методы - это вызываемый вид атрибутов
    info['attributes'] = dir(obj) #  атрибуты , как я понял, номинально вызываемые , но в заданных параметрах вызвать нельзя
    info['module'] = inspect.getmodule(obj)
    print('')
    return info

obj1 = Test(10)
list_test = [42, 'List', introspection_info, Test, obj1]

for l in list_test:
    test_info = introspection_info(l)
    print(test_info)


