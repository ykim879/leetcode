class Solution:
    def numSquares(self, n: int) -> int:
        squares, res = [i ** 2 for i in range (1, int(sqrt(n)) + 1 )], 1
        sums = set(squares)
        while n not in sums:
            res += 1
            nextSum = set()
            for sq in squares:
                for s in sums:
                    s += sq
                    if s == n:
                        return res
                    nextSum.add(s)
            sums.update(nextSum)
        return res
