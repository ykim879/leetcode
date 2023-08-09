class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int: 
        from heapq import heappop, heapify, heappush
        L = len(costs)
        cands = []
        s, e = candidates, max(candidates, L - candidates) - 1
        for i in range(candidates):
            cands.append((costs[i], 0))
        for i in range(e + 1, L):
            cands.append((costs[i], 1))
        heapify(cands)
        res = 0
        for i in range(k):
            c, b = heappop(cands)
            res += c
            if s <= e:
                if b:
                    heappush(cands, (costs[e], 1))
                    e -= 1
                else:
                    heappush(cands, (costs[s], 0))
                    s += 1
        return res

            
