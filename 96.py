class Solution:
    def numTrees(self, n: int) -> int:
        memoized = {0 : 1, 1 : 1}
        def recur(n):
            if n in memoized:
                return memoized[n]
            res = 0
            n -= 1
            k = n//2
            for i in range(k):
                newRes = recur(i) * recur(n - i)
                res += (2 * newRes)
            if n%2:
                res += 2 * (recur(k) * recur(k + 1))
            else:
                res += recur(k) ** 2
            memoized[n + 1] = res
            return res
        return recur(n)
