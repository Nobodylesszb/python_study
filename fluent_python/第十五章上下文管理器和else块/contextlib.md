 ### 构建上下文
自己定义上下文管理器类之前，
先看一下 Python 标准库文档中的“29.6 contextlib Utilities for with-statement contexts”（https://docs.python.org/3/library/contextlib.html）。
除了 前面提到的 redirect_stdout 函数，contextlib 模块中还有一些类和其他函数，使用 范围更广。

- closing

　　如果对象提供了 close() 方法，但没有实现 __enter__/__exit__ 协议，那么可以 使用这个函数构建上下文管理器。

- suppress

　　构建临时忽略指定异常的上下文管理器。

- @contextmanager

　　这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器 协议了。

- ContextDecorator

　　这是个基类，用于定义基于类的上下文管理器。这种上下文管理器也能用于装饰函 数，在受管理的上下文中运行整个函数。

- ExitStack

　　这个上下文管理器能进入多个上下文管理器。with 块结束时，ExitStack 按照后进 先出的顺序调用栈中各个上下文管理器的 __exit__ 方法。如果事先不知道 with 块要进 入多少个上下文管理器，可以使用这个类。例如，同时打开任意一个文件列表中的所有文 件。

显然，在这些实用工具中，使用最广泛的是 @contextmanager 装饰器，因此要格外留 心。这个装饰器也有迷惑人的一面，因为它与迭代无关，却要使用 yield 语句。由此可 以引出协程，这是下一章的主题。