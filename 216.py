class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from copy import copy
        memoized = {}
        def combinationSum(start, k, n):
            if start > 9 or n < start or k < 1 or 10 - start < k:
                return []
            if k == 1:
                if n < 10:
                    return [[n]]
                return []
            key = (start, k, n)
            if key in memoized:
                return copy(memoized[key])
            if 10 - start == k:
                res = [i for i in range(start, 10)]
                if sum(res) == n:
                    memoized[key] = [res]
                    return [res]
                memoized[key] = []
                return []
            res = combinationSum(start + 1, k, n)
            withStart= combinationSum(start + 1, k - 1, n - start)
            for l in withStart:
                ele = copy(l)
                ele.append(start)
                res.append(ele)
            memoized[key] = res
            return copy(res)
        return combinationSum(1, k, n)
            
