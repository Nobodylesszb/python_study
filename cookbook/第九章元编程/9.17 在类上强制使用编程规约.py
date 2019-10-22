"""
元类的一个关键特点是它允许你在定义的时候检查类的内容。在重新定义 __init__() 方法中， 你可以很轻松的检查类字典、父类等等。并且，一旦某个元类被指定给了某个类，那么就会被继承到所有子类中去。 因此，一个框架的构建者就能在大型的继承体系中通过给一个顶级父类指定一个元类去捕获所有下面子类的定义。

作为一个具体的应用例子，下面定义了一个元类，它会拒绝任何有混合大小写名字作为方法的类定义（可能是想气死Java程序员^_^）：
"""
class NoMixedCaseMeta(type):
    def __new__(cls,clsname,bases,clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass = NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):
        pass
    
class B(Root):
    def fooBar(self): # TypeError
        pass