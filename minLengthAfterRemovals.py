class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        end = len(nums)
        l, r = 0, (end + 1) // 2
        while r < end:
            if nums[l] < nums[r]:
                l += 1
                r += 1
            else:
                r += 1
        return end - 2 * l
