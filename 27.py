class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        rightmost = len(nums) - 1
        found = None
        while rightmost >= 0:
            if nums[rightmost] == val:
                nums.pop()
            elif nums[rightmost] != val and rightmost > 0:
                if not found:
                    found = rightmost - 1
                while nums[found] != val:
                    found -= 1
                    if found < 0:
                        return
                # val is found we need to swap with right most
                nums[found] = nums[rightmost]
                nums.pop()
                found -= 1
                if found < 0:
                    return 
            rightmost -= 1
