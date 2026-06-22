class Solution:
    def __init__(self):
        self.__count = list()
    
    def encode(self, strs: List[str]) -> str:
        for s in strs:
            self.__count.append(len(s))
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        ans = list()
        
        l = r = 0
        for c in range(0, len(self.__count)):
            l = r
            r = r + self.__count[c]
            ans.append(s[l:r])
        return ans
