from functools import wraps

# 使用__new__实现单例模式
# class Singleton(object):

#     def __new__ (cls,*args,**kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super().__new__(cls,*args,**kwargs)
#         return cls._instance

# class Test(Singleton):
#     a =1

# b= Test()
# c = Test()
# print(id(b),id(c))

# 使用 装饰器完成单例模式

def Singleton(cls):
    _instance = {}
    @wraps(cls)
    def single(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return single


@Singleton
class Test():
    b =1

a = Test()
b = Test()

print(id(a),id(b))







    