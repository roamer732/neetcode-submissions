class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        large_arr = nums1
        small_arr = nums2

        if len(large_arr) < len(small_arr):
            large_arr, small_arr = small_arr, large_arr

        large_arr_length = len(large_arr)
        small_arr_length = len(small_arr)

        median_index = (large_arr_length + small_arr_length)//2

        # Now we will perform BST in small array to calculate valid partition
        left_index = 0
        right_index = small_arr_length - 1

        while True:
            mid_index = (left_index + right_index)//2
            print("mid_index: ", mid_index)
            partition_index_for_large_arr = median_index - mid_index - 2

            small_arr_leftmost_element_of_partition1 = small_arr[mid_index] if mid_index >= 0 else float("-infinity")
            small_arr_rightmost_element_of_partition2 = small_arr[mid_index+1] if mid_index+1 < small_arr_length else float("infinity")
            large_arr_leftmost_element_of_partition1 = large_arr[partition_index_for_large_arr] if partition_index_for_large_arr >= 0 else float("-infinity")
            large_arr_rightmost_element_of_partition2 = large_arr[partition_index_for_large_arr + 1] if partition_index_for_large_arr + 1 < large_arr_length else float("infinity")

            if large_arr_leftmost_element_of_partition1 <= small_arr_rightmost_element_of_partition2 and \
            small_arr_leftmost_element_of_partition1 <= large_arr_rightmost_element_of_partition2:
                if (large_arr_length + small_arr_length)%2 == 0:
                    return (max(small_arr_leftmost_element_of_partition1, large_arr_leftmost_element_of_partition1) + \
                    min(small_arr_rightmost_element_of_partition2, large_arr_rightmost_element_of_partition2))/2
                else:
                    return min(small_arr_rightmost_element_of_partition2, large_arr_rightmost_element_of_partition2)

            if small_arr_leftmost_element_of_partition1 > large_arr_rightmost_element_of_partition2:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

