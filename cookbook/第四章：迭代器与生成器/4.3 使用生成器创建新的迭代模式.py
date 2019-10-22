"""
问题
你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。

解决方案
如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：
"""

def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment


# if i in frange(0,4,0.5):
#     print(i)

    