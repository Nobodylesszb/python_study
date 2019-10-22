class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

     # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)

if __name__ == "__main__":
    s = Spam(2)
    p = Proxy(s)
    print(p._obj) # <__main__.Spam object at 0x0000025EF5704CF8> 一个实例

    
    