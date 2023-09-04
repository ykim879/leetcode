class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from copy import copy
        nums.sort()
        L = len(nums) - 1
        res = [[]]
        duplicate = 0
        for i, n in enumerate(nums):
            duplicate += 1
            if i < L and n == nums[i + 1]:
                continue
            newRes = []
            for d in range(1, duplicate + 1):
                for r in res:
                    new = copy(r)
                    new.extend([n] * d)
                    newRes.append(new)
            res.extend(newRes)
            duplicate = 0
        return res
