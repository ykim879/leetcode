class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, L = str(s[0]), len(s)
        for i in range(0, L - 1):
            # odd
            end = min(i, L - i - 1) + 1
            l, r = i - 1, i+1
            while l >= 0 and r < L and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l+1: r]
            # even
            l, r = i, i+1
            while l >= 0 and r < L and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l+1: r]
        return res
