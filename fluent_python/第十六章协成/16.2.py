#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 16.2.py 
@version:
@time: 2019/10/22
@function： 产生两个值得协程
"""

from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> start:a:', a)
    b = yield a
    print('-> received: b=', b)
    c = yield a + b
    print('-> received c = ', c)


if __name__ == '__main__':
    my_cora2 = simple_coro2(14)
    print(getgeneratorstate(my_cora2))
    next(my_cora2)
    print(getgeneratorstate(my_cora2))
    my_cora2.send(28)
    my_cora2.send(99)
