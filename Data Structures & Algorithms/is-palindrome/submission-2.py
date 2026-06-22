class Solution:
    def is_alpha_num(self, c: str):
        def is_alpha(c):
            i = ord(c) - ord('a')
            j = ord(c) - ord('A')
            return (i > -1 and i < 27) or (j > -1 and j < 27)
        
        def is_num(c):
            i = ord(c) - ord('0')
            return (i > -1 and i < 10)
        
        return is_alpha(c) or is_num(c)
    
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l <= r:
            while l <= r and not self.is_alpha_num(s[l]):
                l += 1
            while r >= l and not self.is_alpha_num(s[r]):
                r -= 1
            
            if l > r:
                break
            # print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        