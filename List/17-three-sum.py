def threeSum(nums):
    nums.sort()
    size = len(nums)
    three_sum = []
    for i in range(size):
        a= nums[i]
        if i > 0 and a == nums[i-1]:
            continue
        if a>0:
            break
        k = size-1
        j = i+1
        while j<k and nums[k]>=0:
            b= nums[j]
            c= nums[k]
            if(a+b+c==0):
                three_sum.append([a,b,c])
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
            elif(a+b+c<=0):
                j+=1
            else:
                k-=1
    return three_sum

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))