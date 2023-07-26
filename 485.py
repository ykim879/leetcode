class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur = 0
        for n in nums:
            if n:
                cur += 1
            elif cur:
                res = max(res, cur)
                cur = 0
        return max(res, cur)
