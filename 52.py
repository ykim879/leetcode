class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        from copy import copy
        global D
        D = 2 * n - 1
        def nQueens(r, cols, diag1, diag2):
            if not cols or len(diag1) >= D or len(diag2) >= D:
                return 0
            res = 0
            for c in cols:
                if (c+r) not in diag1 and (r-c) not in diag2:
                    if r == n-1:
                        res += 1
                        continue
                    cols_, diag1_, diag2_ = copy(cols), copy(diag1), copy(diag2)
                    cols_.remove(c)
                    diag1_.add(c+r)
                    diag2_.add(r-c)
                    res += nQueens(r+1, cols_, diag1_, diag2_)
            return res
        cols = set([i for i in range(n)])
        return nQueens(0, cols, set(), set())
