"""
问题
你想通过反省或者重写类定义的某部分来修改它的行为，
但是你又不希望使用继承或元类的方式。

解决方案
这种情况可能是类装饰器最好的使用场景了。例如，
下面是一个重写了特殊方法 
__getattribute__ 的类装饰器， 可以打印日志：
"""

def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getarrribute(self,name):
        print('getting:',name)
        return orig_getattribute(self,name)
    
    cls.__getattribute__ = new_getarrribute
    return cls

@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass
    

if __name__ == "__main__":
    a = A(42)
    print(a.x)