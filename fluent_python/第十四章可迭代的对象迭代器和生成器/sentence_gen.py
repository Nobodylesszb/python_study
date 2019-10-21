#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: sentence_gen.py 
@version:
@time: 2019/10/21
@function： 生成器版本
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'sentence({text})'.format(reprlib.repr(text=self.text))

    def __iter__(self):
        for word in self.words: #1
            yield word #2
        return #3

"""
❶ 迭代 self.words。 
❷ 产出当前的 word。 
❸ 这个 return 语句不是必要的；这个函数可以直接“落空”，自动返回。
不管有没有 return 语句，
生成器函数都不会抛出 StopIteration 异常，而是在生成完全部值之后 会直接退出。 6
"""


