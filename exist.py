class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use board as visited
        R, C = len(board), len(board[0])
        def dfs(r, c, i):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "-1":
                return False
            if board[r][c] == word[i]:
                if i == len(word) - 1:
                    return True
                i += 1
                board[r][c] = "-1"
            else:
                return False
            res = dfs(r+1, c, i) or dfs(r-1, c, i) or dfs(r, c+1, i) or dfs(r, c-1, i)
            board[r][c] = word[i-1]
            return res
        for r in range(R):
            for c in range(C):
                if dfs(r,c, 0):
                    return True
        return False
