class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue
            
            if v > 0:
                break
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[l] + nums[r] + v
                if s > 0:
                    r = r -1
                elif s < 0:
                    l = l + 1
                else:
                    res.append([v, nums[l], nums[r]])
                    r = r - 1
                    l = l + 1
                    while nums[l-1] == nums[l] and l < r:
                        l = l + 1
        return res

        