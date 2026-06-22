# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _merge_lists(self, l1, l2): 
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        temp = ListNode()
        head = temp
        while l1 or l2:
            v1 = l1.val if l1 is not None else 1001
            v2 = l2.val if l2 is not None else 1001

            if v1 < v2:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            if len(lists[0]) == 0:
                return None
            return lists[0]
        
        head = lists[0]

        for i in range(1, len(lists)):
            head = self._merge_lists(head, lists[i])
        return head
        