#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: coroaverager3.py 
@version:
@time: 2019/10/22
@function： 委托生成器，子生成器
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():  # !
    total = 0
    count = 0
    average = None
    while True:
        term = yield  # 2
        if term is None:  # 3
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # 4


# 委托生成器
def grouper(results, key):  # 5
    while True:  # 6
        results[key] = yield from averager()  # 7


def main(data):  # 8
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # 9
        next(group)  # 10
        for value in values:
            group.send(value)  # 11
        group.send(None)  # 12 重要


"""
3. 至关重要的终止条件，如果不这样做，使用yield from调用这个协程的生成器会永远阻塞
4. 返回的result会变成group函数中yield from 表达式的值
5. grouper 是委托生成器
6. 这个循环每次迭代会新建一个averager实例。每个实例都会作为协程使用的生成器对象
7. grouper 发送的每个值都会经由yield from 处理，通过管道传给averager实例，grouper会在
yield　from 表达式处暂停，等待averager实例处理客户端发送的值，averagers实例运行完毕后，返回的值
绑定到results[key]上，while 循环会不断创建averager实例 处理更多的值
8. main函数是客户端代码。是驱动一切的函数
9. group 是调用grouper函数得到的生成器函数，传给grouper函数的第一个参数是results
用于收集结果，第二个参数是某个键，group作为协程使用
10.预激grouper协程
11. 把各个value传给grouper，传入的值最后到达average函数中term = yield 哪一行，grouper永远
不知道传入的值是什么
12.把None传入grouper,导致当前的averager实例终止，也让grouper继续运行，再创建一个averager实例
处理下一组值
13 重要，中值当前的averager实例，开始执行下个，如果注释掉那一行，这个脚本不会输出任何报告，此时，把main
函数靠近末尾的print(result)那行去掉，你会发现，results字典为空
"""

"""


"""
