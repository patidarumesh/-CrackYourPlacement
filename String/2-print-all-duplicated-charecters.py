def printAllDuplicates(s):
    size = len(s)
    if size == 0 or size ==1:
        return -1
    dict = {}
    duplicate = []
    for i in s:
        if i in dict.keys() : 
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict:
        if (dict[i])>1:
            duplicate += [(i, dict[i])]
    return duplicate
s = "geeksforgeeks"
print(printAllDuplicates(s))

