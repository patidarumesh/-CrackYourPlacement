def minSwaps( nums):
	sorted_arr = sorted(nums)
	if nums == sorted_arr:
	    return 0
	size = len(nums)
	count = 0
	dict = {}
	for i in range(size):
	    dict[nums[i]]=i
	for i in range(len(nums)):
	    if(nums[i]!=sorted_arr[i]):
	        count +=1
	        a,b = nums[i],sorted_arr[i]
	        nums[i], nums[dict[b]] = nums[dict[b]] , nums[i]
	        dict[a],dict[b] = dict[b], dict[a]
	    
	return count

print(minSwaps([7,16,14,17,6,9,5,3,18]))