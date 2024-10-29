class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # tropotical sorting & bottom to top approach since we do not know the source
        # at node, when we are visiting we are going to update with maximum of longest path starting from there
        memo = [[-1] * len(matrix[0]) for _ in range(len(matrix))]  # Memoization table
        def dfs(r,c, lst):
            # base case: invalid or visited
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= lst:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            cur = matrix[r][c]
            d = max(dfs(r + 1, c, cur), dfs(r, c + 1, cur), dfs(r, c - 1, cur), dfs(r -1 , c, cur))
            d += 1
            memo[r][c] = d
            return d
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        return  max(max(row) for row in memo)
