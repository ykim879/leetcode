class Solution:
    def reverseBits(self, n: int) -> int:
        # for each n % 2 => lowest bit representation -> next lowest//2 
        res = 0
        for _ in range(32):
            res = res * 2 + n % 2
            n = n // 2
        return res
