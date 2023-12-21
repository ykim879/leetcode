class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        L = len(nums)
        nums.extend(nums)
        s = [] # non-increasing stack
        nex = 1
        res = [ -1 for _ in range(L)]
        for i, n in enumerate(nums):
            while s and s[-1][0] < n:
                i_ = s.pop()[1]
                if i_ < L:
                    res[i_] = n
            s.append((n,i))
        return res
