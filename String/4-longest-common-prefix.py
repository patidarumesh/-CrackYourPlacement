def longestCommonPrefix( strs):
        strs.sort()
        first = strs[0]
        last = strs[-1]
        result = ""
        for i in range(len(first)):
            if first[i] == last[i]:
                result+=first[i]
            else:
                break
        return result

print(longestCommonPrefix(["flower","flow","flight"]))