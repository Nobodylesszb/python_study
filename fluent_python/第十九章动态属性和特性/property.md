展开说的话有必要细说一下property的机制，Python当中取对象属性存在多种不同的机制，property属于descriptor机制，在Python当中是一种重要的机制。大致流程是这样的：



set和delete过程也有相应的descriptor机制，不再赘述。



跟重载__getattr__和__setattr__相比，descriptor机制可以很容易改变某几个属性的属性访问机制，而不影响其他属性。

有一些非常重要的功能是通过descriptor实现的，有一些比property更重要也更常用，比如说我们调用类的方法的时候：

```python
class T(object):
    def f(self):
        return 1

t = T()
t.f()
T.f(t)   #等价的
```

使用t.f的时候不需要再指定第一个参数self的值，这就是因为使用了descriptor机制，T.f（在Python2中是unboundmethod，在Python3中是标准的函数）有__get__方法，会将T.f从原来的类型转换成boundmethod，这是一个绑定了第一个参数的函数对象，于是调用时不再需要指定第一个参数。



property也是一样的，首先要知道property本身是个类型，property()是这个类型的构造函数，这个构造函数的原始形式接受(fget, fset, fdel, doc)四个参数，为了方便将property作为decorator使用，所有四个参数都是可选的，这样当作decorator的时候实际是执行了：

```python
width = property(width)
```

也就是仅仅使用了第一个参数构造了property。返回的property对象带有__get__，__set__和__delete__方法，会调用相应的fget, fset和fdelete。为了方便进一步构造，这个对象带有getter, setter, deleter方法，大致是这样的：

```python
def setter(self, fset):
    self.fset = fset
    return self
```

也就是说只是进一步设置了其中的属性然后返回，所以.setter, .deleter都必须使用一致的名字。



了解这个机制之后就可以明白，Python当中的property与其他语言不同，并不是某种特别定制的语法，而是更泛用的descriptor机制的一部分，在任何代码当中调用都会触发这种机制，也包括在property的getter和setter当中调用。这样我们同时也明白了使用obj.__setattr__('width', value)也是不行的，虽然当时看上去好像是成功了，但是会永久改变width这个属性查找时的特性（改由obj.__dict__提供了）。必须占用一个新的属性名，一般我们在Python当中规定_开头的是私有属性，__（两个下划线）开头且不以__结尾的是“强”的私有属性，会被自动重命名为跟类名有关的名字，所以可以用这类名字来做真正存储属性的名字：

```python
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, input_width):
        self._width = input_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, input_height):
        self._height = input_height

    @property
    def resolution(self):
        return self.height * self.width
```

最后，如果仅仅是设置一个值而不引起其他变化，不要定义property比较好。不要学Java程序员那一套。