class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = z = res = 0
        for c in range(len(nums)):
            if not nums[c]:
                z += 1
                while z > k:
                    if not nums[start]:
                        z -= 1
                    start += 1
                print(c, start)
            res = max(res, c - start + 1)
        return res
