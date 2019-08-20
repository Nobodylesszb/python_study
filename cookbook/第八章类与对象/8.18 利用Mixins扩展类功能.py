"""
对于混入类，有几点需要记住。首先是，混入类不能直接被实例化使用。 
其次，混入类没有自己的状态信息，也就是说它们并没有定义 __init__() 方法，
并且没有实例属性。 
这也是为什么我们在上面明确定义了 __slots__ = () 。
"""
from collections import defaultdict


class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging.
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitems__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')

        return super().__setitem__(key, value)


# 使用

class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

if __name__ == "__main__":
    
    d = LoggedDict()
    d['x'] =23
    print(d['x'])

"""
output:
Setting x = 23
Getting x
23
"""