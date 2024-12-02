class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            cur = nums[l] + nums[r]
            if cur == target:
                return [l+1, r+1]
            elif cur < target:
                l += 1
            else:
                r -= 1
