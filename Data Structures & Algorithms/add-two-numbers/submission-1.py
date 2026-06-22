# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        carry = 0

        tail1 = l1
        tail2 = l2

        while tail1 and tail2:
            s = tail1.val + tail2.val + carry
            carry = s//10
            ans.next = ListNode(s%10)
            ans = ans.next
            tail1 = tail1.next
            tail2 = tail2.next
        
        while tail1:
            s = tail1.val + carry
            carry = s//10
            ans.next = ListNode(s%10)
            ans = ans.next
            tail1 = tail1.next
        
        while tail2:
            s = tail2.val + carry
            carry = s//10
            ans.next = ListNode(s%10)
            ans = ans.next
            tail2 = tail2.next
        
        if carry:
            ans.next = ListNode(carry)
        
        return head.next
            
