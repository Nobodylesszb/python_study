"""
一个基本元类通常是继承自 type 
并重定义它的 __new__() 方法 或者是 __init__() 方法。比如：
"""

class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)


class myMeta(type):
    def __init__(self,clsname,bases,clsdict):
        super().__init__(clsname,bases,clsdict)