"""
For strings A, B, when len(A) > len(B), the longest possible subsequence of either A or B is A, and no subsequence of B can be equal to A. Answer: len(A).

When len(A) == len(B), the only subsequence of B equal to A is B; so as long as A != B, the answer remains len(A).

When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.
"""

class Solution(object):
    def findLUSlength(self, a: str, b: str) -> int:
        if  a == b:
            return -1
        return max(len(a),len(b))


        