from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a ** 2)
            if int(b) == b:
                return True
        return False
