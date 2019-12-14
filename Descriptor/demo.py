#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: demo.py 
@version:
@time: 2019/12/15
@function： 
"""


class Property:
    def __init__(self, fget, fset):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)


class C:
    def fget(self):
        print("fget called")

    def fset(self, value):
        print("fset called with", value)

    f = Property(fget, fset)


if __name__ == '__main__':
    c = C()
    print(c.f)
    c.f =1
