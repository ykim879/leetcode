class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k %= len(nums)
        if len(nums) <= 1 or k == 0:
            return
        def reverse(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        reverse(0, len(nums) - 1)
        reverse(0, k -1)
        reverse(k, len(nums) - 1)
            
