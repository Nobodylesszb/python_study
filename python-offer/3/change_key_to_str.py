"""
非字符串的键转换为字符串
"""
import collections

class StrKeyDict(collections.UserDict):
    def __miss__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self,key):
        return str(key) in self.data

    def __setitem__(self,key,item):
        self.data[str(key)] = item


test = StrKeyDict()

test.setdefault(3,6)
print(test)
    
