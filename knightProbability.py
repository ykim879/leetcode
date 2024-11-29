class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        total = 8 ** k
        nextMoves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2,-1)]
        memo = {}
        def recur(count, r, c):
            if not (0<=r<n) or not (0<=c<n):
                return 0
            if count == k:
                return 1
            key = (count, r, c)
            if key in memo:
                return memo[key]
            count += 1
            res = 0
            for i, j in nextMoves:
                res += recur(count, r + i, c + j)
            memo[key] = res
            return res
        return recur(0, row, column) / total
