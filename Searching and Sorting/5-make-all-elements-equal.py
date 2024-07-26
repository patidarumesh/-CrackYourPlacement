def minCost(nums) -> int:
        nums.sort() 
        mid = len(nums) // 2
        median = (nums[mid] + nums[~mid]) // 2
        output = 0
        for num in nums:
            output += int(abs(num-median))
        return output

List = [1,100,101,102]
print(minCost(List))