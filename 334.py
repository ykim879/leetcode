class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #n2 find second smallest where smallest only filled out if n1 has been found. we keep updating finding smallest n2 where smaller n1 has been found before
        n1 = n2 = 2**31
        for n in nums:
            if n > n2:
                return True
            if n < n1:
                n1 = n
            elif n > n1 and n < n2:
                n2 = n
        return False
        
