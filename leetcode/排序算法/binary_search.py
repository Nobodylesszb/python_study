def bin_search(list,val):
    low = 0
    high = len(list)

    while low < high:
        mid = (low + high)//2
        if list[mid] == val:
            return mid
        elif list[mid] > val:
            high  = mid -1
        else:
            low = mid + 1   

    return

#### 迭代二分法

def bin_search_rec(l,value,start=None,end =None):
    start = start if start else 0
    end = end if end else len(l)
    if start <= end:
        mid = (start+end)//2
        if l[mid] == value:
            return mid
        elif l[mid]> value:
            return bin_search_rec(l,value,start,mid-1)
        else:
            return bin_search_rec(l,value,mid+1,end)
    else:
        return None
        
