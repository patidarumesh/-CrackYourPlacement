def subarraySum(nums, k):
    my_dict = {0:1}
    size = len(nums)
    total = 0
    result = 0
    for i in range(size):
        total+=nums[i]
        result += my_dict.get(total-k,0)
        my_dict[total]=my_dict.get(total,0)+1
    return result

nums = [1,2,3]
k = 3
print(subarraySum(nums,k))