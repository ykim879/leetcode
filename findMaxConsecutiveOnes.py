class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = -1
        # (1)we move l until we find first 1
        # (2) we move r from l+1 until we find 0
        # (3) update maximum with these r-l 
        res = 0
        for i, n in enumerate(nums):
            if start >= 0 and n == 0:
                    res = max(res, i - start)
                    start = -1
            elif start < 0 and n == 1:
                    start = i
        return max(res, len(nums) - start) if start >= 0 else res
