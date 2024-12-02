from pprint import pprint
import inspect

class Test():
    def __init__(self, value):
        self.object = object
def introspection_info(obj):
    obj_type = type(obj)
    obj_module = obj.__class__.__module__
    obj_attributes = []
    obj_methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            obj_methods.append(attr)
        elif not callable(getattr(obj, attr)):
            obj_attributes.append(attr)
    info = {'type': obj_type,'module': obj_module, 'attributes': obj_attributes, 'methods': obj_methods, }
    return info

obj1 = Test(10)
list_test = [42, 'List', introspection_info, Test, obj1]

for l in list_test:
    test_info = introspection_info(l)
    print(test_info)


