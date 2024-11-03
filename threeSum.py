class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L, end, i = len(nums) - 1, len(nums) - 3, 0
        res = []
        def move(i):
            while i < len(nums) and nums[i-1] == nums[i]:
                i += 1
            return i
        # pick number from i to len(nums) - 3
        while i <= end:
            target = -1 * nums[i]
            l, r = i+1, L
            while l < r:
                s = nums[l] + nums[r]
                if target == s:
                    res.append([nums[i], nums[l], nums[r]])
                    l = move(l+1)
                    r -= 1
                elif target > s:
                    l += 1
                else:
                    r -= 1
            # move i until [i-1] != [i]
            i = move(i+1) 
        return res        
