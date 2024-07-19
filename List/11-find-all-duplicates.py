def findDuplicates( nums):
        s= set()
        output = []
        for num in nums:
            if num in s:
                output.append(num)
            s.add(num)
        return output

List =[4,3,2,7,8,2,3,1]
print(findDuplicates(List))