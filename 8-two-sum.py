def twoSum( nums, target: int):
        i=j=0
        size = len(nums)
        output = []
        found = False
        for i in range(size-1):
            k = i+1
            for j in range(k,size):
                if(nums[i]+nums[j]==target):
                    output = [i,j]
                    found = True
                    break
                else:
                    j+=1
            if found:
                break
            else:
                i+=1
        return output

List = [2,4,5,7,8,2]
print(twoSum(List, 9))

