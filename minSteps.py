class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # counter(s) and counter(t) should be same
        s, t = Counter(s), Counter(t)
        allcharacters = set()
        allcharacters.update(s.keys())
        allcharacters.update(t.keys())
        # if any are different then we want to find the differences and divide by 2
        res = 0
        for c in allcharacters:
            if s[c] != t[c]:
                res += abs(s[c] - t[c])
        return res//2
