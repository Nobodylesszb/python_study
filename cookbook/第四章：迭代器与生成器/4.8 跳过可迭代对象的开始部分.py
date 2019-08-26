# 问题
# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。

# 解决方案
# itertools 模块中有一些函数可以完成这个任务。 首先介绍的是 itertools.dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，
# 丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素。


from itertools import dropwhile

with open('/cookbook/第七章函数/7.10 带额外状态信息的回调函数.py') as f:
    for line in dropwhile(lambda line:line.startwith('#'),f):
        print(line,end = '')

