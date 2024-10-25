class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # h1 : minheap of (capital, -1 *profit)
        # h2: maxheap of -1 * profit
        h1 = [(capital[i], -1 * profits[i]) for i in range(len(profits))]
        h2 = []
        heapq.heapify(h1)
        for i in range(k):
            while h1 and h1[0][0] <= w:
                c, p = heapq.heappop(h1)
                heapq.heappush(h2, p)
            if not h2:
                return w
            profit = -1 * heapq.heappop(h2)
            w += profit
        return w
