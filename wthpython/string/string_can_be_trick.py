# a = "crazy_python"
# print(id(a))
# print(id("crazy" + "_" + "python"))
"""
output:
41899952
41899952
"""

a =  'crazy'
b = 'crazy'
c = 'crazy!!'
d = 'crazy!!'
e, f = "crazy!", "crazy!"
print (a is b)
print(c is d)
print(e is f)

"""
output:
True
True
True
"""


array_1 = [1,2,3,4]
print(id(array_1))
g1 = (x for x in array_1)
array_1 = [1,2,3,4,5]
print(id(array_1))
"""
output:
41768200
41767048
"""