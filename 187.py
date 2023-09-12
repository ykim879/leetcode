class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        hashed = set()
        for i in range(10, len(s) + 1):
            val = s[i - 10: i]
            if val in hashed:
                res.add(val)
            hashed.add(val)
        return list(res)
