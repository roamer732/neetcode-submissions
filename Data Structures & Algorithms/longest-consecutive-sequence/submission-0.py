class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {n:True for n in nums}
        ans = 0

        for n in nums:
            if n+1 not in h:
                t = 1
                while n-t in h:
                    t += 1
                ans = max(ans, t)
        return ans


        