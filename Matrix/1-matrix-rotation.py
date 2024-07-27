def rotate( matrix):
    size = len(matrix)
    for i in range(size//2):
        for j in range(i, size-i-1):
            temp = matrix[i][j]
            matrix[i][j]=matrix[size-j-1][i]
            matrix[size-j-1][i] = matrix[size-i-1][size-j-1]
            matrix[size-i-1][size-j-1] = matrix[j][size-i-1]
            matrix[j][size-i-1] = temp
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))