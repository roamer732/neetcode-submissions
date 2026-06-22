class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr, fast_ptr = 0, 0
        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break
        
        tail = 0
        while True:
            tail = nums[tail]
            slow_ptr = nums[slow_ptr]
            if tail == slow_ptr:
                break
        return tail
        