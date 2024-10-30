class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        while s < e:
            mid = (s+e) // 2
            # divide with mid and round up if the res > h continue
            res = 0
            for p in piles:
                res += (p + mid - 1) // mid
            if res > h:
                s = mid + 1
            if res <= h:
                e = mid
        return s
