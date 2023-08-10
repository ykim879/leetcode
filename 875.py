class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        piles.sort(reverse= True)
        s, e = 1, piles[0]
        while s < e:
            mid = (s+e) // 2
            # divide with mid and round up if the res > h continue
            res = 0
            for p in piles:
                res += math.ceil(p / mid)
                if res > h:
                    s = mid + 1
                    break
            if res <= h:
                e = mid
        return s
