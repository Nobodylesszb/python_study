"""
问题
作为某种编程规约，你想在对函数参数进行强制类型检查。

解决方案
在演示实际代码前，先说明我们的目标：能对函数参数类型进行断言，类似下面这样：
"""

from functools import wraps
from inspect import signature

import pandas as pd
from pandas import DataFrame

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(
                                name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2, 3)


"""
在装饰器创建的实际包装函数中使用到了 sig.bind() 方法。 
bind() 跟 bind_partial() 类似，
但是它不允许忽略任何参数。因此有了下面的结果
"""


@typeassert(DataFrame)
def test(x):
    print(type(x))
    print(x)


t = pd.DataFrame()

print(test(3))
