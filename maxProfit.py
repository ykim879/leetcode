class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, max_bought, sold, cold = -1000, -1000, -1000, 0
        for p in prices:
            max_bought = max(bought, max_bought)
            bought = cold - p
            cold = max(cold, sold)
            sold = max(sold, max_bought + p)
        return max(cold, sold)
