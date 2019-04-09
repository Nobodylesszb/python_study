"""
using the collections to couter the nums of  apperance of char
"""

import collections

class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])