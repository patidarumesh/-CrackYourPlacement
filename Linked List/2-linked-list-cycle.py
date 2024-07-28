def hasCycle( head):
        my_set = set()
        if head == None:
            return False
        if head.next==None:
            return False
        elif head.next==head:
            return True
        node= head
        while (node.next not in my_set) and node.next is not None:
            my_set.add(node.next)
            node = node.next
        if node.next==None:
            return False
        return True