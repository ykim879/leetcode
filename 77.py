from copy import copy
class Solution(object):
    def __init__(self):
        self.memoized = {}
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        key = (n,k)
        if key in self.memoized:
            res = []
            for l in self.memoized[key]:
                res.append(copy(l))
            return res
        l1 = self.combine(n -1, k -1)
        l2 = self.combine(n - 1, k)
        for l in l1:
            l.append(n)
        l1.extend(l2)
        self.memoized[key] = l1
        return l1
