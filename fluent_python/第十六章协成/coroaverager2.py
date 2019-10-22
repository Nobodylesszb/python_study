#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: coroaverager2.py 
@version:
@time: 2019/10/22
@function： 求平均值的协程
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def average():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)
