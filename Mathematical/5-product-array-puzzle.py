def productExceptSelf(nums, n):
        products = [1]*n
        left  = right =1
        for i in range(n):
            products[i] = left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products

list = [1,2,7,4,6,6,4,2]
n = len(list)

print(productExceptSelf(list, n))