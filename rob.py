class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        ## result can either be with dp[:i-1] or dp[1:i]
        # get dp[:i-1]
        prePre, pre = 0, 0
        for n in nums[:-1]:
            cur = max(prePre + n, pre)
            prePre = pre
            pre = cur
        res = pre
        prePre, pre = 0, 0
        # get dp[1:i]
        for n in nums[1:]:
            cur = max(prePre + n, pre)
            prePre = pre
            pre = cur
        return max(pre, res)
