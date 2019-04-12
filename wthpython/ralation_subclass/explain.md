### 解释
- 在Python中子类的继承关系不一定是传递的，任何人都可以自定义元类（metaclass）中的__subclasscheck__函数（_subclasscheck__(subclass)检查subclass是不是调用类的子类）。
- 当调用issubclass(cls, Hashable)的时候，函数只是简单的检查一下cls和它继承的类中有没有"__hash__"这个方法。
- 因为object是可以被哈希的(也就是说object有__hash__这个函数)，但是list是不能被哈希的，所以他们之间打破了传导关系。
- 如果想看更详尽的解释，[这里](https://www.naftaliharris.com/blog/python-subclass-intransitivity/)有关于Python子类关系传导的详细解释。
- 