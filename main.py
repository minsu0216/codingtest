# input = [['a', 'b'], ['b', 'c'], ['d', 'e'], ['b', 'd']]
# output = ['a', 'c']

import ctypes

a = [1, 2, 3]

oi1 = id(a)
print(oi1)

a = [2, 3, 4]
# oi2 = id(a)
# print(id(a))

def get_object_by_id(object_id):
    obj = ctypes.cast(object_id, ctypes.py_object).value
    
    return obj

c = get_object_by_id(oi1)
print(c[0])