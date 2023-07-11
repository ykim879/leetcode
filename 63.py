class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[R-1][C-1] == 1:
            return 0
        for r in range(R):
            for c in range(C):
                if r == 0 and c == 0:
                    obstacleGrid[r][c] = 1
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
                    continue
                if r > 0 and obstacleGrid[r-1][c] > 0:
                    obstacleGrid[r][c] += obstacleGrid[r-1][c]
                if c > 0 and obstacleGrid[r][c - 1] > 0:
                    obstacleGrid[r][c] += obstacleGrid[r][c - 1]
        return obstacleGrid[R-1][C-1]
