#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: iter_signal.py 
@version:
@time: 2019/10/21
@function： iter 哨符
"""
import random


def signal():
    return random.randint(1, 6)


stop_signal = iter(signal, 1)

if __name__ == '__main__':
    for roll in stop_signal:
        print(roll)
