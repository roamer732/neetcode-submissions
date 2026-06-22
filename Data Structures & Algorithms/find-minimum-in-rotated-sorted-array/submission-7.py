class Solution:    
    def findMin(self, nums: List[int]) -> int:
        array_length = len(nums)       
        left_index = 0
        right_index = array_length - 1

        while left_index < right_index:           
            mid_index = self._get_mid_index(left_index, right_index)
                        
            if self._is_array_not_rotated(nums, mid_index, right_index):
                right_index = mid_index
            else:
                left_index = mid_index + 1
        
        return nums[left_index]
    
    @staticmethod
    def _is_array_not_rotated(nums, l, r):
        return nums[l] < nums[r]
    
    @staticmethod
    def _get_mid_index(left_index, right_index):
        return left_index + (right_index - left_index)//2

        
        