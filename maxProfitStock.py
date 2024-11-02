class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # treat each time price will be max
        min_val = float(inf)
        profit = 0
        for price in prices:
            if min_val > price:
                min_val = price
            elif price - min_val > profit:
                profit = price - min_val
        return profit
