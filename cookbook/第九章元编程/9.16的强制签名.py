# 问题
# 你有一个函数或方法，它使用*args和**kwargs作为参数，
# 这样使得它比较通用， 但有时候你想检查传递进来的参数是不是某个你想要的类型。

# 解决方案
# 对任何涉及到操作函数调用签名的问题，你都应该使用 inspect 模块中的签名特性。 我们最主要关注两个类：Signature 和 Parameter 。
# 下面是一个创建函数前面的交互例子：

from inspect import Signature,Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

class structure:
    __signature__ = make_sig()
    
    def __init__(self,*args,**kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Stock(structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(structure):
    __signature__ = make_sig('x','y')
