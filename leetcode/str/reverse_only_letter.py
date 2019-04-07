"""
Idea is very simple.
Go over the string and construct new string:
by adding non-alphabetic characters or
dumping from "to be reversed" r stack.
"""

class Solution:
    def reverseOnlyLetters(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))