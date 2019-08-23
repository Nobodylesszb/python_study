"""
问题
你在类中需要重复的定义一些执行相同逻辑的属性方法，比如进行类型检查，怎样去简化这些重复代码呢？

解决方案
考虑下一个简单的类，它的属性由属性方法包装：
"""

def typed_property(name,expected_type):
    storage_name = '_' +name

    @property
    def prop(self):
        return getattr(self,storage_name)

    @prop.setter
    def prop(self,value):
        if not isinstance(value,expected_type):
             raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self,storage_name,value)

    return prop


class Person:
    name = typed_property('name',str)
    age = typed_property('age',int)

    def __init__(self,name,age):
        self.name = name
        self.age = age



