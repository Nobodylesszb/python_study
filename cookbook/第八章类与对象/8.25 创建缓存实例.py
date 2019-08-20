"""
问题
在创建一个类的对象时，如果之前使用同样参数创建过这个对象， 你想返回它的缓存引用。

解决方案
这种通常是因为你希望相同参数创建的对象时单例的。 在很多库中都有实际的例子，比如 logging 模块，
使用相同的名称创建的 logger 实例永远只有一个
"""
import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


if __name__ == "__main__":
    s = Spam('dave')
    t = Spam('dava')
    print(s is t)
    """
    Initializing Spam 初始化2次
    Initializing Spam
    False
    """ 