class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, maxidx, END = 0,0, len(nums) - 1
        # while i <= max index: update maxindx if maxindx > len(nums) - 1 return True
        while i <= maxidx:
            maxidx = max(i + nums[i], maxidx)
            if maxidx >= END:
                return True
            i += 1
        return False
