def subarraysDivByK( nums, k):
    prefix = 0
    remainder = {
        0:1,
    }
    size= len(nums)
    result = 0
    for i in range(size):
        prefix = prefix + nums[i]
        x = prefix % k
        result += remainder.get(x,0)
        remainder[x] = remainder.get(x,0)+1
    return result
list = [4,5,0,-2,-3,1]
print(subarraysDivByK(list,5))