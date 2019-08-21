"""
问题
你想使用一个装饰器去包装函数，但是希望返回一个可调用的实例。 你需要让你的装饰器可以同时工作在类定义的内部和外部。

解决方案
为了将装饰器定义成一个实例，你需要确保它实现了 __call__() 和 __get__() 方法。 例如，下面的代码定义了一个类，它在其他函数上放置一个简单的记录层：
"""
import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x,y):
    return x+y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

if __name__ == "__main__":
    print(add(2,3))