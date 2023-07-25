class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter 
        c = Counter(nums)
        res = 0
        for n in c.keys():
            res += min(c[n], c[k-n])
        return res // 2
