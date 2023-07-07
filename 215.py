class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k -= 1
        def swap(i1, i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
        start, end = 0, len(nums) - 1
        while start < end:
            p = start
            target = nums[end]
            for i in range(start, end):
                if target <= nums[i]:
                    swap(p, i)
                    p += 1
            if p == k:
                return target
            swap(p, end)
            if p < k:
                start = p + 1
            else:
                end = p - 1
        return nums[start]
