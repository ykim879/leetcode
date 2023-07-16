import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        h1 = []
        h2 = []
        for i in range(len(profits)):
            if capital[i] <= w:
                heapq.heappush(h2, -1 * profits[i])
            else:
                heapq.heappush(h1, (capital[i], profits[i]))
        for i in range(k):
            if not h2:
                return w
            w += -1 * heapq.heappop(h2)
            while h1 and h1[0][0] <= w:
                heapq.heappush(h2, -1 * heapq.heappop(h1)[1])
        return w
