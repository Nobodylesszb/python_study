
"""
插入算法

每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。

  步骤：

  1. 从第一个元素开始，该元素可以认为已经被排序
  2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
  3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
  4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
  5. 将新元素插入到该位置后
  6. 重复步骤2~5

"""

def insert_sort(list):
    lenth = len(list)
    for index in range(1,lenth):
        key = list[index] #待排序的元素
        j = index -1 
        while j >=0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j-=1
    return list

list = [54,6,23,543,5,2,4]
print(insert_sort(list))

