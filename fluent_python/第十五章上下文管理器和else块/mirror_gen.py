#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: mirror_gen.py 
@version:
@time: 2019/10/25
@function： 
"""
"""
@contextmanager 装饰器能减少创建上下文管理器的样板代码量，
因为不用编写一个完 整的类，定义 __enter__ 和 __exit__ 方法，
而只需实现有一个 yield 语句的生成器， 生成想让 __enter__ 方法返回的值。 
在使用 @contextmanager 装饰的生成器中，yield 语句的作用是把函数的定义体分成两 部分：
yield 语句前面的所有代码在 with 块开始时（即解释器调用 __enter__ 方法 时）执行， 
yield 语句后面的代码在 with 块结束时（即调用 __exit__ 方法时）执行。 
下面举个例子。示例 15-5 使用一个生成器函数代替示例 15-3 中定义的 LookingGlass 类。
"""
import sys
import contextlib


@contextlib.contextmanager  # 1
def look_glass():
    origin_write = sys.stdout.write  # 2

    def reverse_write(text):  # 3
        origin_write(text[::-1])

    sys.stdout.write = reverse_write  # 4
    yield 'abc'  # 5
    sys.stdout.write = origin_write  # 6


"""
1.应用 contextmanager 装饰器。
2. 贮存原来的 sys.stdout.write 方法
3. 定义自定义的 reverse_write 函数；在闭包中可以访问 original_write
4. 把 sys.stdout.write 替换成 reverse_write
5. 产出一个值，这个值会绑定到 with 语句中 as 子句的目标变量上。执行 with 块中的 代码时，这个函数会在这一点暂停
6. 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码；这里是恢复成原来的 sys. stdout.write 方法
"""

