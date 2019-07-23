"""
functools.lru_cache是非常使用的装饰器它实现了备忘录模式
"""

from clock import clock
import functools

# @clock
# def fibonacci(n):
#     if n<2:
#         return n
#     return fibonacci(n-2) + fibonacci(n-1)

# if __name__ == '__main__':
#     print(fibonacci(6))

"""
[0.00000109s]   fibonacci(0)  -> 0
[0.00000109s]   fibonacci(1)  -> 1
[0.00008679s]   fibonacci(2)  -> 1
[0.00000073s]   fibonacci(1)  -> 1
[0.00000146s]   fibonacci(0)  -> 0
[0.00000073s]   fibonacci(1)  -> 1
[0.00003391s]   fibonacci(2)  -> 1
[0.00009956s]   fibonacci(3)  -> 2
[0.00019911s]   fibonacci(4)  -> 3
[0.00000073s]   fibonacci(1)  -> 1
[0.00000073s]   fibonacci(0)  -> 0
[0.00000036s]   fibonacci(1)  -> 1
[0.00001240s]   fibonacci(2)  -> 1
[0.00002407s]   fibonacci(3)  -> 2
[0.00000073s]   fibonacci(0)  -> 0
[0.00000036s]   fibonacci(1)  -> 1
[0.00001130s]   fibonacci(2)  -> 1
[0.00000036s]   fibonacci(1)  -> 1
[0.00000073s]   fibonacci(0)  -> 0
[0.00000036s]   fibonacci(1)  -> 1
[0.00001240s]   fibonacci(2)  -> 1
[0.00002334s]   fibonacci(3)  -> 2
[0.00004558s]   fibonacci(4)  -> 3
[0.00008023s]   fibonacci(5)  -> 5
[0.00029320s]   fibonacci(6)  -> 8
8
"""
"""
浪费时间地方很明显。fibonacci(1)调用了8此，
"""
@functools.lru_cache() # 注意这里带括号。因为lru_cache 可以接收参数
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))

"""
[0.00000146s]   fibonacci(0)  -> 0
[0.00000146s]   fibonacci(1)  -> 1
[0.00014259s]   fibonacci(2)  -> 1
[0.00000292s]   fibonacci(3)  -> 2
[0.00016884s]   fibonacci(4)  -> 3
[0.00000182s]   fibonacci(5)  -> 5
[0.00019437s]   fibonacci(6)  -> 8
8
"""
"""
functool.lru_cache(maxsize =128,typed =false)
"""