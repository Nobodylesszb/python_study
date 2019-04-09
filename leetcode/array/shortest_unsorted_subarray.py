
# a =[1,2,3]
# b= [4,5,6]
# c =zip(a,b)
# print(type(c))
# for a,b in c:
#     print(a,b)

"""
使用
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        is_same = [a==b for a,b in zip(nums,sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

