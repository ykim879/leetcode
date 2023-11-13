class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        if s[0] == '+' or s[0] == '-':
            i += 1
        dotappeared = eappeared = digit = False
        while i < len(s):
            if not s[i].isdigit():
                if s[i] == '.':
                    if dotappeared:
                        return False
                    dotappeared = True
                elif s[i] == 'e' or s[i] == 'E':
                    eappeared = True
                    break
                else:
                    return False
            elif not digit:
                digit = True
            i += 1
        if not digit:
            return False
        if eappeared:
            digit = False
            i += 1
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < len(s):
                if not s[i].isdigit():
                    return False
                elif not digit:
                    digit = True
                i += 1
        return digit
