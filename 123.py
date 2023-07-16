class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        firstTransaction = [0 for i in range(l)]
        secondTrasaction = [0 for i in range(l)]
        basePrice = prices[0]
        for i in range(1,l):
            firstTransaction[i] = max(firstTransaction[i-1], prices[i] - basePrice)
            basePrice = min(basePrice, prices[i])
        basePrice = prices[-1]
        for i in range(l-2, -1, -1):
            secondTrasaction[i] = max(basePrice - prices[i], secondTrasaction[i+1])
            basePrice = max(basePrice, prices[i])
        basePrice = secondTrasaction[0]
        for i in range(1, l-1):
            basePrice = max(basePrice, firstTransaction[i] + secondTrasaction[i+1])
        return basePrice
