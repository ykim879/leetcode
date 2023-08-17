class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from copy import copy
        target = sum(nums)
        if target % 2:
            return False
        target = target // 2
        sums = set([0]) # store all possible sums while we iterate
        for num in nums:
            if num == target:
                return True
            if num > target:
                return False
            nextSums = copy(sums)
            for s in sums:
                s += num
                if s == target:
                    return True
                nextSums.add(s)
            sums = nextSums
        return False
