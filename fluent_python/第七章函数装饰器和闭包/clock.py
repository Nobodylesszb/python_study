'''
简单装饰器的实现
实现计算函数运行时间
'''

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        timepassed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print('[{:.8f}s]   {}({})  -> {}'.format(timepassed, name, arg_str, result))
        return result
    return clocked


@clock
def sleep(sec):
    time.sleep(sec)


@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

if __name__ == '__main__':
    factorial(6)


'''
OUT：

[0.00000146s]   factorial(1)  -> 1
[0.00007075s]   factorial(2)  -> 2
[0.00008752s]   factorial(3)  -> 6
[0.00009810s]   factorial(4)  -> 24
[0.00010904s]   factorial(5)  -> 120
[0.00012289s]   factorial(6)  -> 720

'''
