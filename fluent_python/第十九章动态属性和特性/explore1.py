from collections import abc
import keyword


class FrozenJson:
    def __init__(self, mapping):
        self._data = {}
        for key,value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self._data[key] =value

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return FrozenJson.build(self._data[name])

    @classmethod
    def build(cls, obj):
        # 如果obj是映射。那就构建一个frozenJson对象
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        # 如果obj是MutableSequence对象，必然是列表，我们把obj中的每一个元素递归传给.build（)方法
        # 构建一个列表
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        # 如果既不是字典也不是列表。那么原封不动的返回元素
        else:
            return obj

if __name__ == "__main__":
    x = FrozenJson({'2b3':'or not'})
    print(x)

            
