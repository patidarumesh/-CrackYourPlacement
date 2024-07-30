def maxArea( height):
    size = len(height)
    i=0
    j= size-1
    capacity = 0
    while i < j:
        curr_capacity = (j-i)* min(height[i], height[j])
        capacity = max(capacity,curr_capacity)
        if(height[i] > height[j]):
            j -=1
        else:
            i+=1
    return capacity

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))