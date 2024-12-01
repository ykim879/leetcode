class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            nextRow = [1]
            for i2 in range(1, i):
                nextRow.append(res[-1][i2 - 1] + res[-1][i2])
            nextRow.append(1)
            res.append(nextRow)
        return res
