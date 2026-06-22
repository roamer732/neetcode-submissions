class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._left = Node(0, 0)
        self._right = Node(0, 0)
        self._left.next = self._right
        self._right.prev = self._left
        self._cache = dict()
    
    def _remove(self, node):
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev
    
    def _insert(self, node):
        node.next = self._right
        node.prev = self._right.prev
        self._right.prev = node
        node.prev.next = node
        
    def get(self, key: int) -> int:
        if key in self._cache:
            self._remove(self._cache[key])
            self._insert(self._cache[key])
            return self._cache[key].val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._remove(self._cache[key])
        node = Node(key, value)
        self._insert(node)
        self._cache[key] = node

        if len(self._cache) > self._capacity:
            least_recently_used = self._left.next
            self._remove(least_recently_used)
            del self._cache[least_recently_used.key]
