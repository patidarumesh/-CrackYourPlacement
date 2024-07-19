# Brute force 
# def subarraysDivByK(nums, k: int) -> int:
        
#         output = 0
#         for i in range(len(nums)):
#             subarray = []
#             j = i
#             while j <len(nums):
#                 subarray.append(nums[j])
#                 if sum(subarray)%k == 0:
#                     output +=1
#                 j +=1
            
#         return output

# Reduced time complexity
def subarraysDivByK( nums, k):

        count = {0: 1}  # Initialize with count of subarray sum 0
        total_sum = 0
        result = 0

        for num in nums:
            total_sum += num
            remainder = total_sum % k

            # Convert negative remainder to positive
            remainder = remainder if remainder >= 0 else remainder + k

            # If remainder exists in the count dictionary,
            # add its count to the result
            result += count.get(remainder, 0)

            # Increment the count of the current remainder
            count[remainder] = count.get(remainder, 0) + 1

        return result
List = [4,5,0,-2,-3,1]
# List = [-5]
k = 5
print(subarraysDivByK(List,k))