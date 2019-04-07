"""
反转字符串中每一个字符
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in str.split(' '):
            result.append(word[::-1])
        return " ".join(result)


str = "ab'c efg bcd"

S =Solution()
print(S.reverseWords(str))

        