class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, comps: List[List[int]], stock: List[int], costs: List[int]) -> int:
        res = 0
        for comp in comps:
            arr = [stock[i]//comp[i] for i in range(n)]
            max_ = max(arr) + 1
            start, end = max(res, min(arr)), budget // max(1, sum([comp[i] * costs[i] for i in range(n)])) + max_
            if end <= start:
                res = start
                continue
            base = -1 * sum([stock[i] * costs[i] for i in range(n)])
            k = sum([comp[i] * costs[i] for i in range(n)])
            while start <= end:
                print(comp, start, end)
                mid = (end + start) // 2
                cost = 0
                if mid < max_:
                    cost = sum([max(comp[i] * mid - stock[i], 0) * costs[i] for i in range(n)])
                else:
                    cost = base + k * mid
                if cost == budget:
                    start = mid
                    break
                elif cost < budget:
                    if start == end:
                        break
                    if start == mid:
                        start = mid + 1
                    else:
                        start = mid
                else:
                    if start == end:
                        start -= 1
                        break
                    end = mid - 1
            res = max(res, start)
        return res
