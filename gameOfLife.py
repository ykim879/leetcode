# beats 84%
from copy import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        rows = [[0]*len(board[0]) for i in range(len(board))]
        res = copy(board)
        for r in range(ROW):
            for c in range(COL):
                if c == 0:
                    rows[r][c] = board[r][c]
                else:
                    rows[r][c] = rows[r][c-1]
                if c - 2  >= 0:
                    rows[r][c] -= board[r][c-2]
                if c + 1 < COL:
                    rows[r][c] += board[r][c+1]
        for r in range(ROW):
            for c in range(COL):
                neighbors = rows[r][c]
                if r > 0:
                    neighbors += rows[r-1][c]
                if r < len(board) - 1:
                    neighbors += rows[r+1][c]
                if board[r][c] == 0 and neighbors == 3:
                    res[r][c] = 1
                elif board[r][c] == 1 and (neighbors <= 2 or neighbors > 4):
                    res[r][c] = 0
        return res
        
