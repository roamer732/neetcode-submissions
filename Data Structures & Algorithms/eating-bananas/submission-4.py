class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right_index = max(piles)
        left_index = 1
        k = max(piles)

        while left_index <= right_index:
            mid_index = left_index + (right_index-left_index)//2

            eating_hour = 0
            for p in piles:
                eating_hour = math.ceil(p/mid_index) + eating_hour

            if eating_hour > h:
                left_index = mid_index + 1
                continue
            
            if k > mid_index:
                k = mid_index
            right_index = mid_index - 1
        return k
