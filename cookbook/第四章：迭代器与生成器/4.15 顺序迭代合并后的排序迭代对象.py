# 问题
# 你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。

# 解决方案
# heapq.merge() 函数可以帮你解决这个问题

import heapq

a = [1,4,7,10]
b = [2,4,6,8]
for c in heapq.merge(a,b):
    print(c)

"""

1
2
4
4
6
7
8
10
"""

#heapq.merge 可迭代特性意味着它不会立马读取所有序列。 这就意味着你可以在非常长的序列中使用它，而不会有太大的开销


with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)