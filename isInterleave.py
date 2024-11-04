class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # loop over each i pointer s1[:i]
        # dp[j] = max(s1[i] == s3[i+j] and prevdp[i-1, j], s2[i] == s3[i+j] and prevdp[i, j-1])
        L1, L2 = len(s1), len(s2)
        dp = [False for _ in range(L2 + 1)] # avoid j-1 contarint 
        dp[0] = True
        # initialize first row
        for j in range(1, L2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, L1 + 1): # means how many s1 is used
            dp[0] = s1[i-1] == s3[i-1] and dp[0]
            for j in range(1, L2 + 1): # means how many s2 is used
                c = i + j - 1
                dp[j] = max(s1[i - 1] == s3[c] and dp[j], s2[j - 1] == s3[c] and dp[j-1])
        return dp[-1]
