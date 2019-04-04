#算法逻辑比较简单，以第一个list为基准，第二个向第一个插空

def merge_sort(list1,list2):
    lenth_list1 = len(list1)
    lenth_list2 = len(list2)
    list3  = []
    j = 0 
    for i in range(lenth_list1):
        while list2[j]<list1[i] and j < lenth_list2 :
            list3.append(list2[j])
            j +=1
        list3.append(list1[i])
    if j <(lenth_list2):
        for k in range(j,lenth_list2):
            list3.append(list2[k])
    return list3

list1=[1,3,5,10]
list2=[2,4,6,8,9,11,12,13,14]
print(merge_sort(list1,list2))