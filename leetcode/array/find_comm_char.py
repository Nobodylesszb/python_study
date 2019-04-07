import collections

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())


s = Solution()

list1 = ["bella","label","roller"]

print(s.commonChars(list1))
        