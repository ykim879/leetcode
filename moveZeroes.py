class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, L = 0, 1, len(nums)
        while r < L:
            if l == r or nums[r] == 0:
                r += 1
            elif nums[l] != 0:
                l += 1
            else:
                nums[l] = nums[r]
                nums[r] = 0
