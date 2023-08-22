class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        C = len(matrix[0])
        s, e = 0, len(matrix) * C - 1
        while s <= e:
            mid = (s+e) // 2
            r, c = divmod(mid, C)
            cur = matrix[r][c]
            if cur == target:
                return True
            if cur < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
