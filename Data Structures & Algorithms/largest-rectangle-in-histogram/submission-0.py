class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        st = []     # pair (i, h)

        for i, h1 in enumerate(heights):   
            last = i      
            while st and st[-1][1] > h1:
                j, h2 = st.pop()
                maxA = max(maxA, (i-j)*h2)
                last = j
            st.append((last, h1))
        
        for i, h in st:
            maxA = max(maxA, (len(heights)-i)*h)
        return maxA