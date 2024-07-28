class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    fast = head
    slow = head
    count = 0
    while fast is not None:
        count += 1
        if count % 2 == 0:
            slow = slow.next
        fast = fast.next            
    return slow

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
print("Original linked list:")
print_linked_list(head)

middle = middleNode(head)
print("\nMiddle node value:")
print(middle.val)


