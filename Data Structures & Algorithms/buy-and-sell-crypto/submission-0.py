class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 1
        buy_value = prices[l-1]
        while l < len(prices):
            if prices[l] < buy_value:
                buy_value = prices[l]
            else:
                max_profit = max(max_profit, prices[l]-buy_value)
            l += 1
        return max_profit
        