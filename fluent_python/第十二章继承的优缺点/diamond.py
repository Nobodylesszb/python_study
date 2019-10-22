#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: diamond.py 
@version:
@time: 2019/10/21
@function： 继承mro表实验
"""


class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)


class C(A):
    def pong(self):
        print('PONG', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping', self)

    def pingping(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    print(d.pong())
    print(C.pong(d))
    """
    pong <__main__.D object at 0x105617f90>
    None
    PONG <__main__.D object at 0x105617f90>
    None
    """
