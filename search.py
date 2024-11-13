class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search: target is within start and end range
        ## start > end: 
        ### mid: start < mid: target is within this value end = mid else: start = mid
        ### mid : start > mid: target is within mid and end: start = mid else: end = mid
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            start, end, mid = nums[l], nums[r], nums[m]
            if nums[m] == target:
                return m
            if start > end:
                if start <= mid:
                    if start <= target < mid:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if mid < target <= end:
                        l = m + 1
                    else:
                        r = m - 1
            ## start < end:  mid < target: start = mid else: end = mid
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        return l if nums[l] == target else -1
