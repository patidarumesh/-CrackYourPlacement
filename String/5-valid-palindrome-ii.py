def validPalindrome( s):
    i=0
    j=len(s)-1
    while i<=j:
        if s[i]!=s[j]:
            first=s[:i]+s[i+1:]
            second=s[:j]+s[j+1:]
            return first==first[::-1] or second==second[::-1]
        i+=1
        j-=1
    return True
print(validPalindrome('cbabbc'))