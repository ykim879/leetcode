class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #ascending and descending if n[i-1] > n[i] then n[i] is the minimum
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if min(nums[m-1], nums[m], nums[m+1]) != nums[m-1]:
                return min(nums[m], nums[m+1])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
