class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 2 x 3 x -2 : [6, -2], 4 cur, res, stack, minus = True
        # [-2, 0, -1] if zero, emtpy the stack
        res, max_, min_ = max(nums), 1, 1
        for n in nums:
            n_max = max_ * n
            n_min = min_ * n
            max_ = max(n_max, n_min, n)
            min_ = min(n_max, n_min, n)
            res = max(res, max_)
        return res
            
