def twoSum(nums, target):
    my_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in my_dict:
            return [my_dict[diff], i]
        my_dict[num] = i
    return None

nums = [-1,-2,-3,-4,5]
target = 3
print(twoSum(nums,target))