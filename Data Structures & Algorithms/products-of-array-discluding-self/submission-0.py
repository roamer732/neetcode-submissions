class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]*(len(nums)+2)
        m = 1
        for i in range(len(nums)):
            p[i+1] = nums[i] * m
            m = p[i+1]
        
        m = 1
        ans = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            ans[i] = m * p[i]
            m = m*nums[i]
        return ans


        