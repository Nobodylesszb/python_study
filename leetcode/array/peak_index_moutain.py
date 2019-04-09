class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for index in range(len(A)):
            if A[index] < A[index +1]:
                continue
            else:
                return index