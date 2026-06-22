# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        size = 0
        tail = head
        while tail:
            size += 1
            tail = tail.next
        
        if size == n:
            if n == 1:
                return None
            return head.next
        
        target_index = size - n - 1
        tail = head
        while target_index > 0:
            target_index -= 1
            tail = tail.next
        tail.next = tail.next.next
        return head