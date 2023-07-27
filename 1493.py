class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deletion, start, res = -1, 0, 0
        for i, c in enumerate(nums):
            if not c:
                if deletion == -1:
                    deletion = i
                else:
                    res = max(i - start - 1, res)
                    start = deletion + 1
                    deletion = i
        return max(res, len(nums) - start - 1)
