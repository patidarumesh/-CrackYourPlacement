# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def removeDuplicates(nums):
    size = len(nums)
    i=0
    while i<=size-2:
        if nums[i]==nums[i+1]:
            nums.pop(i+1)
            size -=1
        else:
            i +=1
        
    return size

list = [2,2,2,3,5,67,8,8,7]
print(removeDuplicates(list))

        
