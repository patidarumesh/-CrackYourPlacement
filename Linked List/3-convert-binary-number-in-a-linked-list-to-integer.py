class Solution(object):
    def getDecimalValue(self, head):
        string = ''
        node = head
        while node:
            string+= str(node.val)
            node = node.next
        num = int(string,2)
        return num