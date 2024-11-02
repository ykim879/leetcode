class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        hq = [[-1 * count, c] for c, count in counter.items()]
        heapq.heapify(hq)
        prev = heapq.heappop(hq)
        prev[0] += 1
        res = "" + prev[1]
        while hq:
            c, ele = heapq.heappop(hq)
            res += ele
            if prev[0] < 0:
                heapq.heappush(hq, prev)
            prev = [c+1, ele]
        if len(s) > len(res):
            return ""
        return res
