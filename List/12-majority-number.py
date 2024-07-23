def majorityElement( nums):
        nums.sort()
        size = len(nums)
        return nums[size//2]

print(majorityElement([2,2,3,3]))