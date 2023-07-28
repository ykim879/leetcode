class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        n = len(grid)
        rows, cols = Counter(), Counter()
        for i in range(n):
            rows[tuple(grid[i])] += 1
            cols[tuple([grid[r][i] for r in range(n)])] += 1
        res = 0
        for key, val in rows.items():
            if key in cols:
                res += val * cols[key]
        return res
