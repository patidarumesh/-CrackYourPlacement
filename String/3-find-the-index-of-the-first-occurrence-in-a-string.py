def strStr(haystack, needle):
        b = len(needle)
        for i in range(len(haystack)- len(needle)+1):
            print(haystack[i:i+b])
            if haystack[i:i+b] == needle:
                return i
        return -1
        
        
print(strStr("saddsaf", "saf"))