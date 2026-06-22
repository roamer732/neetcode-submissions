class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()
        l = 0
        maxChar = 0
        res = 0
        for idx in range(len(s)):
            freq[s[idx]] = 1 + freq.get(s[idx], 0)
            maxChar = max(maxChar, freq[s[idx]])
            if (idx-l+1)-maxChar <= k:
                res = max(res, (idx-l+1))
            else:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
        return res