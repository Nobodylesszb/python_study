# 选择排序
"""
它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置
 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
 重复第二步，直到所有元素均排序完毕。
"""

def select_sort(list):
    lenth = len(list)
    for index in range(lenth):
        for j in range(index,lenth):
            if list[index]>list[j]:
                list[index],list[j] = list[j], list[index]
    return list

list = [54,6,23,543,5,2,4]

print(select_sort(list))