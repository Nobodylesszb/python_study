## orm
### type
- type(name, bases, attrs)
  - name：class的名称；
    bases：继承的父类集合,以tuple形式传入；
    attrs：class的方法名称与函数绑定，
    注：通过type()函数创建的类和直接写class是完全一样的。当Python解释器遇到class定义时，检查class定义的语法，然后也是调用type()函数创建出class。
  
### metaclass
type()可以实现动态创建类，但是要控制类的创建行为，需要使用metaclass。metaclass直译为元类，元类是用来定义类的，metaclass必须继承type。先定义metaclass，然后创建class，最后class类创建实例。

利用metaclass创建类，需要用到 __new__魔术方法，new魔法方法是在init方法之前调用的，其参数如下：

1. 当前准备创建的类cls；
2. 类的名字；
3. 类继承的父类集合；
4. 类的方法集合
