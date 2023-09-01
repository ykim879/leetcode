class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        res = [[0 for i in range(n)] for i in range(n)]
        mid = n//2
        for start in range(mid):
            end = n - start
            c = end - 1
            for i in range(start, end):
                res[start][i] = count
                count += 1
            for i in range(start + 1, end):
                res[i][c] = count 
                count += 1
            for i in range(c - 1, start - 1, -1):
                res[c][i] = count
                count += 1
            for i in range(c - 1, start, -1):
                res[i][start] = count
                count += 1
        if n % 2:
            res[mid][mid] = count
        return res
