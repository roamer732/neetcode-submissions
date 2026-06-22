class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        f = dict()
        for n in nums:
            if n not in f:
                f[n] = 1
            else:
                f[n] += 1
        
        h = [list() for i in range(len(nums)+1)]
        for key, v in f.items():
            # print(v, key)
            h[v].append(key)
            # print(h)
        ans = []
        for i in range(len(nums), -1, -1):
            if not h[i]:
                continue
            for n in h[i]:
                ans.append(n)
                # print(len(ans), ans, k)
                if len(ans) == k:
                    return ans

        