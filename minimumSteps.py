class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = l = 0
        L = len(s)
        # find l where black ball first occured
        while l < L and s[l] == "0":
            l += 1
        r = l + 1
        # find while ball next to the first black ball
        while r < L:
            if s[r] == "0":
                count += r - l
                l += 1 # l will point to next black ()
            r += 1
        return count
