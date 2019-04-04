# 冒泡算法
"""
1.比较相邻的元素，如果第一个比第二个大，就交换他们两个
2.对每个相邻元素做同样的工作，从开始第一对到最后一对，这步完成后，最后的元素会成为最大的数
3.针对所有的元素重复以上的步骤，除去最后一个
3.持续每次对越来越少的元素重复上述的步骤，直到没有一堆元素进行比较
"""

def bubble_sort(list):
    lenth = len(list)
    for index in range(lenth):
        for j in range(1,lenth-index):
            if list[j-1]>list[j]:
                list[j-1] ,list[j] = list[j],list[j-1]
    return list


list = [54,6,23,543,5,2,4]

print(bubble_sort(list))