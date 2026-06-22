class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = dict()
        for s in strs:
            c = [0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            k = tuple(c)
            if k in r:
                r[k].append(s)
            else:
                r[k] = [s]
        return r.values()
        
        