class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        
        node = head
        while node and node.next    :
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
            
        return head