class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        st = []
        l = 0
        for c in s:
            if c in ["(", "{", "["]:
                st.append(c)
                continue
            
            if not st or st[-1] != self.get_corresponding_character(c):
                return False
            st.pop()
        
        return len(st) == 0

    def get_corresponding_character(self, c: str):
        return {")":"(", "}":"{", "]":"["}.get(c)

        