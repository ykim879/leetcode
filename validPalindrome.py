class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False, l, r
                l += 1
                r -= 1
            return True, l, r
        res, l, r = isPalindrome(0, len(s) - 1)
        return res or isPalindrome(l+1, r)[0] or isPalindrome(l, r-1)[0]
