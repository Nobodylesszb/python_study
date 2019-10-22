#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: bo
@file: 16.2.py
@version:
@time: 2019/10/22
@function： 预激装饰器
"""

from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer
