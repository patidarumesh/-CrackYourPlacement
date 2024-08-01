def fourSum(nums, target):
    nums.sort()
    size = len(nums)
    result = []
    
    for i in range(size - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, size - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k, l = j + 1, size - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    while k < l and nums[k] == nums[k + 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1
                    k += 1
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    
    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
