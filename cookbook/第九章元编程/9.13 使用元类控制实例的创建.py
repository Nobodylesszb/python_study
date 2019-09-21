import weakref
#元类单例模式

class Singleton(type):
    def __init__(self, *args, **kwargs):
        print('_____')
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass = Singleton):
    def __init__(self):
        print('creating spam')




"""
creating spam
True
"""


#创建缓冲实例

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Test(metaclass = Cached):
    def __init__(self,name):
        print('creating spam{!r}'.format(name))
        self.name = name

if __name__ == "__main__":
    # a = Spam()
    # b =Spam()
    # print(a is b)
    a =Test('a')
    b = Test('b')
    c = Test('a')
    print(a is b)
    print(a is c)