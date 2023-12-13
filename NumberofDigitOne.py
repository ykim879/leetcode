class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        i = 1
        while i <= n:
            d = i * 10
            res += (n // d) * i + min(max(n % d - i + 1, 0), i)
            ## (n // d) * i : number of digit '1' at ones place
            # min(max(n % d - i + 1, 0), i): remaining 
            i *= 10
        return res
