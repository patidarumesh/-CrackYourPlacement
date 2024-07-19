class Solution:
    def findDuplicate(self,nums):
        x = set()
        
        for i in nums:
            if i in x:
                return i 
            x.add(i)
        return -1
if __name__ == '__main__':
    List = [6,4,6,8,9,6,6,43]
    sol = Solution()
    print(sol.findDuplicate(List))