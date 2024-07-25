def ceil_num(list,num):
    if num in list:
        return num
    size = len(list)
    low = 0
    high = size-1
    while (low <= high):
        mid = low + (high - low) / 2
        mid = int(mid)
        if (list[mid] == num):
            return mid
        elif (num < list[mid]):
            high = mid - 1
        else:
            low = mid + 1
 
    return low
    
    

list = [1,2]
print(ceil_num(list,2))
