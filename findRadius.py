class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        i, L = 0, len(heaters)
        houses.sort()
        heaters.sort()
        gap = 0
        for h in houses:
            while i < L - 1 and heaters[i+1] <= h:
                i += 1
            if i < L - 1:
                gap = max(gap, min(abs(h - heaters[i]), heaters[i+1] - h))
            else:
                gap = max(gap, abs(h - heaters[i]))
        return gap
