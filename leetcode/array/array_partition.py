"""
Consider the smallest element x. 
It should be paired with the next smallest element, because min(x, anything) = x, and having bigger elements only helps you have a larger score. Thus,
we should pair adjacent elements together in the sorted array.
"""

class Solution:
    def arrayPairSum(self,A):
        return sum(sorted(A)[::2])