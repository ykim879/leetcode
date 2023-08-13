class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # hold: state of maximum profit when it is holding a stock among prices[:i+1] -> current hold can be replaced if previous cumulative profit - prices[i] is bigger
        # free: cumulative maximum profilt among prices[:i+1]
        hold, free = -prices[0], 0
        for i in range(1, len(prices)):
            temp = free
            free = max(free, hold + prices[i] - fee)
            hold = max(hold, temp - prices[i])
        return free
