#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: sentence_genexp.py 
@version:
@time: 2019/10/21
@function： 生成器版本
"""
import re
import reprlib

RE_WORDS = re.compile('\w+')


class Sentece:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'sentence{text}'.format(text=reprlib.repr(self.text))

    def __iter__(self):
        return (match.group() for match in RE_WORDS.finditer(self.text))
