class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = minSum = nums[0]
        total = curSum1 = curSum2 = 0
        for n in nums:
            curSum1 = max(curSum1, 0)
            curSum2 = min(curSum2, 0)
            curSum1 += n
            curSum2 += n
            total += n
            maxSum = max(maxSum, curSum1)
            minSum = min(minSum, curSum2)
        if total == minSum:
            return maxSum
        return max(maxSum, total - minSum) 
