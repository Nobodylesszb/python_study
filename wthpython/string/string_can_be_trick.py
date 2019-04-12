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