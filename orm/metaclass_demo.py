#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: metaclass_demo.py 
@version:
@time: 2019/12/14
@function：元类
"""


class Person(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        return type.__new__(cls, name, bases, attrs, **kwargs)
        # 此处的type，也可以用super()来代替
        #return super().__new__(cls, name, bases, attrs, **kwargs)


class User(metaclass=Person):
    def __init__(self, name):
        self.name = name
        super().__init__()
    def __str__(self):
        return self.name


user = User('apple')
print(user.name) # 'apple'
