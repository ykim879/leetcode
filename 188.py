class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        profits = [[0 for _ in range(l)] for _ in range(k + 1)]
        for i in range(1, k+1):
            buy = -1001
            for j in range(1, l):
                buy = max(buy, profits[i-1][j-1] - prices[j-1])
                profits[i][j] = max(profits[i][j-1], prices[j] + buy)
        return profits[k][l-1]
