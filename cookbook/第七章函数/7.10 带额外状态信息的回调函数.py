# 问题
# 你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)， 并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。

# 解决方案
# 这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用——特别是跟异步处理有关的。 为了演示与测试，我们先定义如下一个需要调用回调函数的函数：

def apply_async(func,args,*,callback):
    result = func(*args)

    callback(result)

def print_result(result):
    print('Got',result)

def add(x,y):
    return x+y

apply_async(add, (2, 3), callback=print_result)


