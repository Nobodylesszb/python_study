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