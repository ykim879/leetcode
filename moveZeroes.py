class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, L = 0, 1, len(nums)
        # find l value where it is 0
        while l < L:
            if nums[l] == 0:
                break
            l += 1
        r = l + 1
        while r < L:
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        while l < L:
            nums[l] = 0
            l += 1
"""
less intuitive but cleaner but less time complexity
  def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, L = 0, len(nums)
        for right in range(L):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        while left < L:
            nums[left] = 0
            left += 1
"""
