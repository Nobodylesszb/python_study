class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2:
            return True
        isGreat = False
        isLess = False
        for i in range(1,n):
            if A[i-1] > A[i]:
                isGreat = True
            if A[i-1] < A[i]:
                isLess = True
            if isGreat and isLess:
                return False
        return True
