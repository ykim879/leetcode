class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [ -1 for _ in range(n)]
        start = sorted([(v[0], i) for i, v in enumerate(intervals)])
        end = sorted([(v[1], i) for i, v in enumerate(intervals)])
        j, i = 0, 0
        while j < n:
            if end[i][0] > start[j][0]:
                j += 1
            else:
                res[end[i][1]] = start[j][1]
                i += 1
                if i == n:
                    break
        return res
