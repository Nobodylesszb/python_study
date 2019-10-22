"""
问题
你想同时迭代多个序列，每次分别从一个序列中取一个元素。

解决方案
为了同时迭代多个序列，使用 zip() 函数。比如：
"""

from itertools import zip_longest
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62]
print(list(zip(xpts,ypts)))
for x,y in zip(xpts,ypts):
    print(x,y)

"""
output:
[(1, 101), (5, 78), (4, 37), (2, 15), (10, 62)]
1 101
5 78
4 37
2 15
10 62
"""
from itertools import zip_longest

a = [1,2,3]
b = ['w','x','y','z']

for i in zip_longest(a,b,fillvalue=0):
    print(i)

"""
output:
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')
"""




