class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # (1) construct max array
        L = len(nums)
        maxRight = [0] * L
        maxRight[-1] = nums[-1]
        for i in range(L - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], nums[i])
        # (2) move l and r 
        l, width = 0, 0
        for r in range(1, L):
            # calculate width
            if maxRight[r] >= nums[l]:
                width = r - l
            else:
                l += 1
        return width
