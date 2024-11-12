class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Solution: 
        ## (1) sorted nums enumerate first
        ## (2) second: binarysearch where  second element = first elemnt + k 
        nums = Counter(nums)
        res = 0
        for n, c in nums.items():
            if (n+k) == n:
                res += c > 1
            else:
                res += (n+k) in nums
        return res
