from collections import abc
import keyword


class FronzenJson:

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            # 默认的行为是委托给超类的__new__方法，这里是调用object基类的__new__方法，把唯一的参数设为fromzenJson
            return super().__new__(cls)

        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]

        else:
            return arg

    def __init__(self, mapping):
        self._data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self._data[key] = value

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return FronzenJson(self._data[name])

"""
__new__方法的第一个参数是类，因为创建的对象通常那个类的实例
所以，在FrozenJson.__new__方法中，super().__new__(cls)表达式
会调用object.__new__(frozenjson).而object类构造的实例其实是frozenjson
的实例，即那个实例的__class__属性储存的是FronzenJson类的引用，不过，真正
的构造操作由解释器调用c语言实现的object.__new__犯法实现的
"""