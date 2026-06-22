"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        hash_map = dict()
        tail = head
        while tail:
            node = Node(tail.val)
            hash_map[tail] = node
            tail = tail.next
        
        tail = head
        node = hash_map[head]
        while tail:
            if tail.next is not None:
                node.next = hash_map[tail.next]
            if tail.random is not None:
                node.random = hash_map[tail.random]
            tail = tail.next
            node = node.next

        return hash_map[head]
        