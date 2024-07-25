def permuteArrays(a, b, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i]+b[i] < k:
            return False
    return True

a = [7,6,9]
b= [1,3,4]
k=10
print(permuteArrays(a,b,k))