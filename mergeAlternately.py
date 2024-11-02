class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, L1, L2 = 0, len(word1), len(word2)
        for i in range(min(L1, L2)):
            res += word1[i]
            res += word2[i]
        if L1 < L2:
            res += word2[L1:]
        elif L2 < L1:
            res += word1[L2:]
        return res
