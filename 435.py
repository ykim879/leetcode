class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end, res = -5 * 10**4, 0
        for s, e in intervals:
            if s < end:
                res += 1
                end = min(e, end)
            else:
                end = e
        return res
