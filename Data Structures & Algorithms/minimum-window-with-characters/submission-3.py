class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq = dict()
        for i in t:
            freq[i] = 1 + freq.get(i, 0)

        matches = 0
        l = 0
        ans = ""
        minL = len(s)
        for i in range(len(s)):
            if s[i] not in freq:
                continue
            
            freq[s[i]] -= 1
            if freq[s[i]] >= 0:
                matches += 1
            
            while matches == len(t):
                if (i-l+1) <= minL:
                    ans = s[l:i+1]
                    print(ans)
                    minL = i - l + 1
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        matches -= 1
                l += 1
        return ans
                
            


        