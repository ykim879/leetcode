class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        from heapq import heappop, heappush
        hq = [(m[0][0], 0, 0)]
        n, MAX = len(m), 10**9 + 1
        m[0][0] = MAX
        for _ in range(k-1):
            _, x, y = heappop(hq)
            if x < n - 1 and m[x+1][y] < MAX:
                heappush(hq, (m[x+1][y], x+1, y))
                m[x+1][y] = MAX
            if y < n - 1 and m[x][y+1] < MAX:
                heappush(hq, (m[x][y+1], x, y+1))
                m[x][y+1] = MAX
        return heappop(hq)[0]

        
