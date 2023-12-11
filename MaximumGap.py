class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(0, len(nums) - 1):
            if nums[i+1] - nums[i] > res:
                res = nums[i+1] - nums[i]
        return res
