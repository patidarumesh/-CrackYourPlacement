def search( nums, target):
    i = 0
    j = len(nums) - 1
    while i<=j:
        if nums[i] == target:
            return i
        i += 1
    return -1

print(search([4,5,6,7,0,1,2],6))