class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        cur = 0
        vowels = set([ 'a', 'e', 'i', 'o', 'u'])
        for i, c in enumerate(s):
            if c in vowels:
                cur += 1
            if i >= k and s[i-k] in vowels:
                cur -= 1
            res = max(cur, res)
        return res
