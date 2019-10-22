#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: sentence_iter.py 
@version:
@time: 2019/10/21
@function：正确的迭代器
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 1

        return SentenceIterator(self.words)  # 2


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # 3
        self.index = 0  # 4

    def __next__(self):
        try:

            word = self.words[self.index]  # 5

        except IndexError:

            raise StopIteration()  # 6

        self.index += 1  # 7
        return word  # 8

    def __iter__(self):  # 9
        return self


"""
❶ 与前一版相比，这里只多了一个 __iter__ 方法。这一版没有 __getitem__ 方法，为 的是明确表明这个类可以迭代，因为实现了 __iter__ 方法。 
❷ 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器。 
❸ SentenceIterator 实例引用单词列表。 
❹ self.index 用于确定下一个要获取的单词。 
❺ 获取 self.index 索引位上的单词。 
❻ 如果 self.index 索引位上没有单词，那么抛出 StopIteration 异常。 
❼ 递增 self.index 的值。 
❽ 返回单词。 
❾ 实现 self.__iter__ 方法。

"""
