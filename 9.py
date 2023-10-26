class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        s, e = 0, len(x) - 1
        while s < e:
            if x[s] != x[e]:
                return False
            s += 1
            e -= 1
        return True
