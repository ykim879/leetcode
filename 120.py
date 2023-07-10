class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for r in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[r])):
                triangle[r][i] += min(triangle[r + 1][i:i+2])
        return triangle[0][0]
            
