# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        merged_list_head = list1
        if list1.val > list2.val:
            merged_list_head = list2

        while list1 and list2:
            if list1.val > list2.val:
                while list2.next and list1.val >= list2.next.val:
                    list2 = list2.next
                temp = list2.next
                list2.next = list1
                list2 = temp
            else:
                while list1.next and list2.val >= list1.next.val:
                    list1 = list1.next
                temp = list1.next
                list1.next = list2
                list1 = temp
        return merged_list_head
            

