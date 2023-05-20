class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= 2:
            return s
        
        res = ""
        row = 0
        def skippedCal(r):
            if r == 0:
                return r
            if r == 1:
                return 2
            return (r - 1) * 2 + 2
        for r in range(numRows):
            c = r
            skip = skippedCal(numRows - r - 1)
            reverse = skippedCal(r)
            forward = True
            while c < len(s):
                print(s[c], forward, skip, reverse)
                res += s[c]
                if not skip:
                    c += reverse
                    forward = False
                elif not reverse:
                    c += skip
                    forward = True
                elif forward:
                    c += skip
                    forward = False
                elif not forward:
                    c += reverse
                    forward = True      
        return res
                
