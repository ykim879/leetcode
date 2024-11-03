class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter of s and t are the same
        s, t = Counter(s), Counter(t)
        for key in s.keys() | t.keys():
            if s[key] != t[key]:
                return False
        return True
