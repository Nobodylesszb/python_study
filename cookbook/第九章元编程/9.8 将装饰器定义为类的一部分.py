"""
问题
你想在类中定义装饰器，并将其作用在其他函数或方法上。

解决方案
在类里面定义装饰器很简单，但是你首先要确认它的使用方式。
比如到底是作为一个实例方法还是类方法。 下面我们用例子来阐述它们的不同：
"""

from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 1')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapper
