class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) + 1
        start, cur = -1, 0
        for i, n in enumerate(nums):
            if n >= target:
                return 1
            elif start == -1:
                cur = n
                start = i
            else:
                cur += n
                while cur - nums[start] >= target:
                    cur -= nums[start]
                    start += 1
                if cur >= target:
                    res = min(res,i - start + 1)
        if res == len(nums) + 1 :
            return 0
        return res
