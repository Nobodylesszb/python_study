"""
问题
你用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值。

解决方案
先看下下面代码的效果：
"""

func = [lambda x:x+n for n in range(5)]

for f in func:
    print(f(0))

"""
4
4
4
4
4
"""

funcs = [lambda x,n=n:x+n for n in range(5)]

for f in funcs:
    print(f(0))


"""
0
1
2
3
4
"""