# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        tail = head
        while prev:
            t1 = tail.next
            t2 = prev.next

            tail.next = prev
            prev.next = t1

            prev = t2
            tail = t1
        
        if tail:
            tail.next = None
        