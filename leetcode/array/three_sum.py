"""
firstly, we accumulate the sum for A.
i.e. Input: A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
we got lista = [0, 2, 3, -3, 3, -4, 5, 6, 8, 8, 9]
total == a[-1] == 9, each sum of one part is 9 // 3 = 3, second is 3 * 2 = 6
we just need ensure that 3 and 6 are both in a, and 6 is rightside of 3.
"""

import itertools


class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        a = list(itertools.accumulate(A)) # 叠加a
        total = sum(A)
        if total % 3 != 0:
            return False
        one = total // 3
        two = one * 2
        if one in a:
            l_index = a.index(one)
        else:
            return False
        if two in a[l_index:]:
            return True
            # r_index = len(A) - 1 - a[::-1].index(two)
        else:
            return False