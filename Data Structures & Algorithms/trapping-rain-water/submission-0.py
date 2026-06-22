class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = height[0], height[len(height)-1]
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            if height[l] < r_max:
                if height[l] < l_max:
                    ans += min(r_max, l_max)-height[l]
                l += 1
                l_max = max(height[l], l_max)
            else:
                if height[r] < r_max:
                    ans += min(l_max, r_max)-height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return ans

        