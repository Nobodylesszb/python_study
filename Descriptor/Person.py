#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: Person.py 
@version:
@time: 2019/12/15
@function： 关于property使用
"""
import re


class Person:
    def __init__(self):
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        m = re.match('\w+@\w+\.\w+', value)
        if not m:
            raise Exception('email not valid')
        self._email = value

    @email.deleter
    def email(self):
        del self._email

if __name__ == '__main__':
    print(Person.email)



