#元类单例模式

class Singleton(type):
    def __init__(self, *args, **kwargs):
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


if __name__ == "__main__":
    a = Spam()
    b =Spam()
    print(a is b)

"""
creating spam
True
"""