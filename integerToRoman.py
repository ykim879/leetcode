class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def toRoman(decimal, d):
            print(decimal, d)
            if d == 0:
                return ""
            if decimal == 0:
                m = "V"
                n = "I"
                k = "X"
            elif decimal == 1:
                m = "L"
                n = "X"
                k = "C"
            elif decimal == 2:
                m = "D"
                n = "C"
                k = "M"
            else:
                m = n = "M" 
            if d == 5:
                return m
            elif d < 4:
                return n * d
            elif d < 5:
                return n * (5-d) + m
            elif d < 9:
                return m + n * (d-5)
            else:
                return n * (10 - d) + k
        decimal = 0
        res = ""
        while num >= 10 ** decimal:
            res = toRoman(decimal, (num % (10 ** (decimal + 1))//10**decimal)) + res
            decimal += 1
        return res
