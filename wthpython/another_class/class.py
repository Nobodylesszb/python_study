class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]
    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]

some_obj = SomeClass(420)
print(some_obj.some_list,some_obj.another_list)
"""
output:
[5, 420] [5, 420]
"""
another_obj = SomeClass(111)
print(another_obj.some_list,another_obj.another_list)

"""
output:
[5, 111] [5, 420, 111]
"""
print(another_obj.another_list is SomeClass.another_list)
print(another_obj.another_list is some_obj.another_list)
"""
output:
True
"""

