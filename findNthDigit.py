class Solution:
    def findNthDigit(self, n: int) -> int:
        # d is digit, start is currently cummulated sequence that starts from current digit, total is current cumulated
        start, total, d = 0, 9, 1
        while total < n:
            start = total + 1
            total += (10 ** (d+1) - 10 ** d) * (d+1)
            d += 1
        number, i = divmod(n - start, d)
        if d > 1:
            number += 10 ** (d-1)
        return int(str(number)[i])
