class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # prefix and postfix
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res
