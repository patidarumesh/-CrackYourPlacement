def minMoves2(nums) -> int:
        nums.sort() 
        mid = len(nums) // 2
        median = (nums[mid] + nums[~mid]) // 2
        output = 0
        for num in nums:
            output += int(abs(num-median))
        return output

List = [1,10,2,9]
print(minMoves2(List))