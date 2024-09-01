from pprint import pprint
import inspect

info = {}
attributes = []
methods = []

class Test():
    def __init__(self, value):
        self.object = object

def introspection_info(obj):
    for i in dir(obj):
        if i.startswith('_'):
            methods.append(i)
        else:
            attributes.append(i)

        info[type.__name__] = type(obj)
        info['methods'] = methods
        info['attributes'] = attributes
        info['module'] = inspect.getmodule(obj)
    return info

obj1 = Test(10)
list_test = [42, 'List', introspection_info, Test, obj1]

for l in list_test:
    test_info = introspection_info(l)
    print(test_info)


