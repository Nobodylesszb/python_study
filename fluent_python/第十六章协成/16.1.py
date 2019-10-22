#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 16.1.py 
@version:
@time: 2019/10/22
@function： 最基本的协成
"""


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

if __name__ == '__main__':
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)
    my_coro.send(42)


"""
<generator object simple_coroutine at 0x000001F1955D4468>
-> coroutine started
-> coroutine received: 42
"""