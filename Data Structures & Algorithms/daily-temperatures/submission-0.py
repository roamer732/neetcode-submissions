class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):          
            while st and temperatures[st[-1]] < t:
                ans[st[-1]]=(i-st[-1])
                st.pop()
            if not st or temperatures[st[-1]] >= t:
                st.append(i)
                continue
        return ans
            
        