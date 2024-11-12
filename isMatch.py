class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        L1, L2 = len(s), len(p)
        dp = [[False] * (L2 + 1) for _ in range(L1 + 1)]
        # base case: dp[0][0] = True  dp[1:][0] = False dp[0][1:] = if will be false if it not having * 
        dp[0][0] = True
        for j in range(2, L2+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(L1):
            for j in range(L2):
                ## (1)star: "preceding chracter" is matching s[i] (p[j-1] == s[i] and dp[i-1][j] # consider star is already populated) or dp[i][j-2] (zero preceding element)
                if p[j] == "*":
                    dp[i+1][j+1] = max((p[j-1] == s[i] or p[j-1] == '.')and dp[i][j+1], dp[i+1][j-1])
                elif p[j] == '.' or p[j] == s[i]: ## (2) non start (p[j] == '.' or p[j] == s[i]) and dp[i-1][j-1]
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = False
        return dp[L1][L2]
