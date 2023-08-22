class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        pcount, scount = Counter(), Counter()
        L = len(p)
        res = []
        for c in p:
            pcount[c] += 1
        for i, c in enumerate(s):
            if i >= L:
                scount[s[i-L]] -= 1
            scount[c] += 1
            if scount == pcount:
                res.append(i - L + 1)
        return res
