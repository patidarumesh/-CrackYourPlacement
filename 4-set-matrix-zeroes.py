# https://leetcode.com/problems/set-matrix-zeroes/description/
list = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zeroes = []
for i, single_list in enumerate(list):
    for j, num in enumerate(single_list):
        if single_list[j] == 0:
            zeroes.append((i,j))

for row,col in zeroes:
    list[row] = [0 for i in list[row]]
for row,col in zeroes:
    for i in list:
        i[col] = 0
