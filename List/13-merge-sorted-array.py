def merge( nums1, m, nums2, n):
    for i in range(n):
          nums1[i+m] = nums2[i]
    nums1.sort()
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,3,nums2,3))