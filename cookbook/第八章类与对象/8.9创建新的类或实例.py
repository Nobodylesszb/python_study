# 你想创建一个新的拥有一些额外功能的实例属性类型
# 比如类型检查


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('excepted an int')
        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        del instance.__dict__[self.name]


class piont:
    x = Integer('x')
    y = Integer('y')

    def __init__(self,x,y):
        self.x =x
        self.y =y

if __name__ == "__main__":
    p = piont(2,3)
    print(p.x)
    print(p.y)
    p.x = 2.3
    print(p.x)


"""

Traceback (most recent call last):
  File "/Users/bo/Documents/project/python_study/cookbook/第八章类与对象/8.9创建新的类或实例.py", line 36, in <module>
    p.x = 2.3
  File "/Users/bo/Documents/project/python_study/cookbook/第八章类与对象/8.9创建新的类或实例.py", line 17, in __set__
    raise TypeError('excepted an int')
TypeError: excepted an int
"""