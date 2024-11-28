class Solution:
    def hammingWeight(self, n: int) -> int:
        # for each time do % 2. then floor division the n
        res = 0
        while n > 0:
            res += n % 2
            n = n // 2
        return res
