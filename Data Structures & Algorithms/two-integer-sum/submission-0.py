class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        h = dict()
        for i, n in enumerate(nums):
            j = h.get(target-n)
            if j is not None:
                return [j, i]
            h[n] = i
        return [0, 0]
        