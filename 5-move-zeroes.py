def moveZeroes(nums):
    size = len(nums)
    i=0
    while i <= size-2:
        if nums[i]==0:
            nums.pop(i)
            nums.append(0)
            size -=1
        else:
            i +=1
    return nums
print(moveZeroes([7,5,7,9,9,0,3,0,0,45,7,8,5]))