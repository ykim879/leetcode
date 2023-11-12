class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        def recur(cands, k) -> str:
            n = len(cands)
            if n == 1 or k == 1:
                return ''.join(cands)
            if k == 0:
                return ''.join(cands[::-1])
            f = factorial(n-1)
            start = k//f
            end = k % f
            if end == 0:
                start -= 1
            nextcands = cands[:start] + cands[start + 1:]
            return cands[start] + recur(nextcands, k % f)
        recurList = [str(i) for i in range(1,n+1)]
        return recur(recurList, k)
        
