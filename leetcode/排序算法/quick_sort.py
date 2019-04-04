"""
快速排序**

- 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。
- 从数列中挑出一个元素，称为”基准”（pivot），
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""

# def quick_sort(list):
#     less = []
#     pivotlist = []
#     more = []
    
#     if len(list) <= 1:
#         return list
#     else:
#         pivot = list[0]
#         for i in list:
#             if i < pivot:
#                 less.append(i)
#             elif i > pivot:
#                 more.append(i)
#             else:
#                 pivotlist.append(i)
#     less = quick_sort(less)
#     more = quick_sort(more)
#     return less + pivotlist + more 


# 方法二

def quick_sort(list):
    if (len(list)) <= 1:
        return list
    else:
        pivot = list[0]

        return quick_sort([x for x in list[1:]if x < pivot]) + [pivot] + quick_sort([x for x in list[1:] if x >= pivot])


list = [54,6,23,543,5,2,4]

print(quick_sort(list))

