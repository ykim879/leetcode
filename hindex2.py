class Solution:
    def hIndex(self, c: List[int]) -> int:
        L = len(c)
        start, end = 0, L - 1
        res = 0
        while start <= end:
            mid = (start + end) // 2
            before, times = mid - 1, L - mid
            if before >= 0:
                before = c[before]

            if times >= before and times <= c[mid]:
                return times
            if before > times:
                end = mid - 1
            else:
                start = mid + 1
        
        return res
