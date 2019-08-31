"""
问题
你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器， 但是它的参数太多了，导致调用时出错。

解决方案
如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。 partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。 为了演示清楚，假设你有下面这样的函数：

"""
from functools import partial

def spam(a,b,c,d):
    print(a,b,c,d)


s1 =partial(spam,1)
print(s1(3,4,5))
