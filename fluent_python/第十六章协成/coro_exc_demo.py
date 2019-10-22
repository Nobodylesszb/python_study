#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: coro_exc_demo.py 
@version:
@time: 2019/10/22
@function：协程异常处理
"""


class DemoException(Exception):
    """
    """
    pass


def demo_exc_handing():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('demoexception handled continuing')

        else:
            print('-> coroutine received:{!r}'.format(x))

    raise RuntimeError('this line should never run ')
