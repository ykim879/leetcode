class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use three dictionaries row/column/square where key indicate which and value is set
        # if ever we have duplicate in set it will return false
        d = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                v = board[r][c]
                if v == ".":
                    continue
                c, s= c + 9, 18 + r//3 * 3 + c//3
                if v in d[r] or v in d[c] or v in d[s]:
                    return False
                d[r].add(v)
                d[c].add(v)
                d[s].add(v)
        return True
