def diff_exist(arr,x):
    unique = set()
    for i in arr:
        if i+x in unique:
            return 1
        if i-x in unique:
            return 1
        unique.add(i)
    return -1

list = [2,5,7,8,9,5,3,80]
print(diff_exist(list,79))
