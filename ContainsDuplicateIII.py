class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # take advantage of range by dividing and index increment only one by one
        d = {}
        valueDiff += 1
        for i, v in enumerate(nums):
            k = v // valueDiff
            if k in d or ((k - 1) in d and (v - d[k-1]) < valueDiff) or ((k + 1) in d and (d[k+1] - v) < valueDiff):
                return True
            d[k] = v
            if i >= indexDiff: # d will have one value for each time
                d.pop(nums[(i - indexDiff)] // valueDiff)
        return False
