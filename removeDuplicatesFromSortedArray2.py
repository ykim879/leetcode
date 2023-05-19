class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #right pointer going to count the occurence, left is current max
        left , right = 1, 1
        occ = 1
        prev = nums[0]
        # right will always indicate what should be praced in left
        while right < len(nums):
            if prev == nums[right]:
                occ += 1
                if occ > 2: # if occurence has been over twice, right has to find new value to replace in left
                    while prev == nums[right]:
                        right += 1
                        if right >= len(nums): #cannot find current left valid replacement
                            return left
                    prev = nums[right]
                    occ = 1
            else:
                occ = 1
                prev = nums[right]
            nums[left] = nums[right]
            left += 1
            right += 1
        return left
