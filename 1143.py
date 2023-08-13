class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        # m will represent lcs between texts1[:c] and text2[:r]
        m = [[0 for i in range(l1 + 1)] for i in range(l2 + 1)]
        for r in range(1, l2 + 1):
            for c in range(1, l1+1):
                if text1[c - 1] == text2[r - 1]:
                    m[r][c] = max(m[r-1][c-1] + 1, m[r][c-1])
                else:
                    m[r][c] = max(m[r-1][c], m[r][c-1])
        return m[-1][-1]
