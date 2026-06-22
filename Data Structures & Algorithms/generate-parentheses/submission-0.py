class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(i: int, j: int, p: str):
            if j > i:
                return
            
            if j == n:
                ans.append(p)
                return
            
            if i < n:
                generate(i+1, j, p+"(")
            generate(i, j+1, p+")")
        generate(0, 0, "")
        return ans