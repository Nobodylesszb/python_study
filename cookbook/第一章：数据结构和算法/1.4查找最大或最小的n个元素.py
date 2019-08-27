"heap模块有两个函数，nlargest(),nsmallest"
import heapq
nums = [1,8,2,2,3,7,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

"""
[42, 37, 23]
[1, 2, 2]
"""
print(heapq.heapify(nums))