"""
问题
你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。

解决方案
函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作。比如：
"""
import itertools
def count(n):
    while True:
        yield n
        n +=1

c = count(0)
# print(c[10:20])  #TypeError: 'generator' object is not subscriptable

for x in itertools.islice(c,10,20):
    print(x)

"""
10
11
12
13
14
15
16
17
18
19
"""
