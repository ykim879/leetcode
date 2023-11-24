class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        dp = [[0 for _ in range(S)] for _ in range(T)]
        for r in range(T):
            for c in range(r, S):
                if s[c] == t[r]:
                    if r > 0 and c > 0:
                        dp[r][c] += dp[r-1][c-1]
                    else:
                        dp[r][c] += 1
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        return dp[-1][-1]
