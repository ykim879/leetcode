class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] < nums[end]: # all sorted
                return nums[start]
            i = (start + end + 1) // 2
            if i > 0 and nums[i-1] > nums[i]:
                return nums[i]
            if i == 0 and nums[-1] < nums[0]:
                return nums[-1]
            if nums[i] > nums[end]:
                start = i + 1
            elif nums[start] > nums[i]:
                end = i - 1
            else:
                start += 1
                end -= 1
        if start < len(nums):
            return nums[start]
        return nums[0]
