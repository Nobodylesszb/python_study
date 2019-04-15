"""
using the collections to couter the nums of  apperance of char
"""

import collections

class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])



class Solution1(object):
    def firstUniqChar(self, s):
        sc = collections.Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0) == 1:
                return i
        return - i


st = 'adsgssfdfd'

s= Solution1()
print(s.firstUniqChar(st))