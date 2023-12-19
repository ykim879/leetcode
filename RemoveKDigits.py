class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = [] # monolithic increasing ordered stack
        for n in num:
            while s and s[-1] > n and k > 0:
                s.pop()
                k -= 1
            s.append(n)
        # remove left-over times
        while s and k > 0:
            s.pop()
            k -= 1
        if not s:
            return "0"
        # remove leading 0
        start = 0
        while start < len(s) and s[start] == "0":
            start += 1
        if start == len(s):
            return "0"
        
        return "".join(s[start:])
