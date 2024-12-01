class Solution:
    def rotateImage(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            end = n - 1 - i
            for c in range(n-1-2*i):
                matrix[i][i + c], matrix[end - c][i], matrix[end][end - c], matrix[i + c][end] = matrix[end - c][i], matrix[end][end - c], matrix[i + c][end], matrix[i][i + c]
