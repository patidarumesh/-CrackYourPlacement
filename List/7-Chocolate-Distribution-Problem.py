def findMinDiff( A,N,M):
    difference = 34567890876543213456789654321456786543276543
    A.sort()
    i=0
    while i < N-M+1:
        difference = min(A[i+M-1]- A[i], difference)
        i +=1
    return difference

A = [8 ,9, 7]
N = len(A)
M = 2
print(findMinDiff(A,N,M))