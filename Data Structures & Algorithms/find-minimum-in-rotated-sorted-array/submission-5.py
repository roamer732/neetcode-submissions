class Solution:    
    def findMin(self, nums: List[int]) -> int:
        array_length = len(nums)
        # if array_length == 1:
        #     return nums[0]
        
        left_index = 0
        right_index = array_length - 1
        
        if self._is_array_not_rotated(nums, left_index, right_index):
            return nums[0]

        while left_index <= right_index:
            if left_index == right_index:
                return nums[left_index]
            
            if abs(left_index-right_index) == 1:
                return min(nums[left_index], nums[right_index])
            
            mid_index = self._get_mid_index(left_index, right_index)
            if not self._is_array_not_rotated(nums, left_index, mid_index):
                right_index = mid_index
                continue
            
            if not self._is_array_not_rotated(nums, mid_index, right_index):
                left_index = mid_index
                continue
    
    @staticmethod
    def _is_array_not_rotated(nums, l, r):
        return nums[l] < nums[r]
    
    @staticmethod
    def _get_mid_index(left_index, right_index):
        return left_index + (right_index - left_index)//2

        
        