class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        from math import log
        n = 0
        cur = 0
        for i in range(len(chars)):
            n += 1
            if i == len(chars) - 1 or chars[i] != chars[i+1]:
                chars[cur] = chars[i]
                cur += 1
                if n > 1:
                    new_len = int(log(n + 0.1, 10)) # there is weird in python math log
                    for k in range(new_len, -1, -1):
                        chars[cur] = str((n % 10 ** (k + 1)) // 10 ** k)
                        cur += 1
                n = 0
        return cur
