class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        # k is the distance between left and right.
        # at least one element needs to be there to calculate middle
        for k in range(2, n): 
            for left in range(0, n - k):
                right = left + k
                max_ = dp[left][right]
                for i in range(left + 1,right): #milddle
                    max_ = max(max_, nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                dp[left][right] = max_
        return dp[0][n - 1]
