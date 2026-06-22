class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        freq = [0]*128
        left = 0
        for right in range(len(s)):
            freq[ord(s[right])] += 1
            while freq[ord(s[right])] > 1:
                freq[ord(s[left])] -= 1
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length
        