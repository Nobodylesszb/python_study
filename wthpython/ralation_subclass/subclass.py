from collections import Hashable
print(issubclass(list,object))
print(issubclass(object,Hashable))
print(issubclass(list,Hashable))

"""
output:
True
True
False
"""