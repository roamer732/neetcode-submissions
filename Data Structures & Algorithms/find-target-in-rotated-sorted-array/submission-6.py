class Solution:
    def search(self, nums: List[int], target: int) -> int:
        array_length = len(nums)            
        left_index = 0
        right_index = array_length - 1


        while left_index <= right_index:
            mid_index = self._get_mid_index(left_index, right_index)

            if nums[mid_index] == target:
                return mid_index
            
            if self._is_array_sorted_in_given_range(nums, mid_index, right_index):
                if self._is_target_exist_in_given_range(nums, target, mid_index, right_index):
                    left_index = mid_index + 1
                else:
                    right_index = mid_index        
            else:
                if self._is_target_exist_in_given_range(nums, target, left_index, mid_index):
                    right_index = mid_index
                else:
                    left_index = mid_index + 1

        return -1

    @staticmethod
    def _is_target_exist_in_given_range(arr, target, l, r):
        return arr[l] <= target and arr[r] >= target
    
    @staticmethod
    def _get_mid_index(l, r):
        return l + (r - l)//2
    
    @staticmethod
    def _is_array_sorted_in_given_range(arr, l, r):
        return arr[l] < arr[r]
        