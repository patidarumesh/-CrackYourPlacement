def threeSum(nums):
    my_dict = {}
    three_sum = []
    size = len(nums)
    for i in range(size):
        for j in range(i+1,size):
            for k in range(j+1,size):
                my_dict[nums[k]] = k
                diff = -(nums[i]+nums[j])
                if diff in my_dict:
                    three_sum.append([nums[i],nums[j],nums[k]])
                    my_dict = {}
                    break
            my_dict = {}
    return three_sum

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))