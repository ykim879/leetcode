class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calculate(i):
            lo = op = None
            while i < len(s):
                if s[i].isdigit():
                    start = i
                    while i < len(s) - 1 and s[i+1].isdigit():
                        i += 1
                    if lo and op:
                        if op == "+":
                            lo += int(s[start:i + 1])
                        else:
                            lo -= int(s[start : i + 1])
                        op = None
                    else:
                        lo = int(s[start : i + 1])
                        if op == "-":
                            lo *= (-1)
                elif s[i] == "(":
                    i += 1
                    if lo and op:
                        ro, i = calculate(i)
                        if op == "+":
                            lo += ro
                        else:
                            lo -= ro
                        op = None
                    else:
                        lo, i = calculate(i)
                        if op == "-":
                            lo *= (-1)
                elif s[i] == ")":
                    return lo, i
                elif s[i] != " ":
                    op = s[i]
                i += 1
            return lo, i
        res = calculate(0)[0]
        return res
