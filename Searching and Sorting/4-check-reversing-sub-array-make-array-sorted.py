def check_reversing_subarray(nums):
    sorted_arr = sorted(nums)
    if sorted_arr == nums:
        return True
    size = len(nums)
    i = 0
    j= size-1
    while nums[i] == sorted_arr[i] and i<size:
        i+=1
    while nums[j]==sorted_arr[j] and j>=0:
        j-=1
    while nums[j] == sorted_arr[i] and i<=j:
        if(i<j):
            j -=1
            i+=1
        elif(i>=j):
            return True
        

    return False

print(check_reversing_subarray([1, 2, 4, 5, 3 ]))