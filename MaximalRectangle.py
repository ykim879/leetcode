class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        from collections import deque
        # 1. calculate the histo of each row: from current row calculate the rectagle
        # 2. from that histo calculate the max histogram
        # *. enge case: how to deal with 0
        R, C = len(matrix), len(matrix[0])
        maxRect = 0
        for r in range(R):
            s = []
            left = []
            for c in range(C):
                if r > 0 and matrix[r][c] == "1":
                    matrix[r][c] = matrix[r-1][c] + 1
                elif r == 0 and matrix[r][c] == "1":
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = 0
                cur = matrix[r][c]
                while s and s[-1][1] >= cur:
                    s.pop()
                if s:
                    left.append(s[-1][0] + 1)
                else:
                    left.append(0)
                s.append((c,cur))
            s = []
            for c in range(C-1, -1, -1):
                cur = matrix[r][c]
                while s and s[-1][1] >= cur:
                    s.pop()
                if s:
                    maxRect = max(maxRect, (s[-1][0] - left[c]) * cur)
                else:
                    maxRect = max(maxRect, (C - left[c]) * cur)
                s.append((c,cur))
        return maxRect
