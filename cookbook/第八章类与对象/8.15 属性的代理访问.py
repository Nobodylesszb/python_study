"""
问题
你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式。

解决方案
简单来说，代理是一种编程模式，它将某个操作转移给另外一个对象来实现。 最简单的形式可能是像下面这样：
"""

class A:
    def spam(self,x):
        pass

    def foo(self):
        pass

class B1:
    def __init__(self):
        self._a = A()

    def spam(self,x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass

"""
如果仅仅就两个方法需要代理，
那么像这样写就足够了。但是，如果有大量的方法需要代理， 那么使用 __getattr__() 方法或许或更好些：
"""
class B2:
    """使用__getattr__的代理，代理方法比较多时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)