
"""
你想将一个只读属性定义成一个property，
并且只在访问的时候才会计算结果。 
但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
"""

import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls): 
        if instance is None:
            return self

        else:
            value = self.func(instance) # instance 表示要执行的实例
            setattr(instance, self.func.__name__, value)
            return value

"""
self: lazy 的实例
instance:circle的实例
cls：circle 类
"""
class circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    c = circle(4)
    print(c.radius)
    print(c.area)
    print(c.area)
    print(c.perimeter)
    print(c.perimeter)


"""
4
Computing area
50.26548245743669
50.26548245743669
Computing perimeter
25.132741228718345
25.132741228718345
"""