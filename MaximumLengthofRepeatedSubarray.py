class Solution(object):
    def findLength(self, A, B):
        L1, L2 = len(A), len(B)
        dp = [[0 for _ in range(L2)] for _ in range(L1)]
        #populate zero index 
        for r in range(L1):
            if A[r] == B[0]:
                dp[r][0] = 1
        for c in range(1, L2):
            if A[0] == B[c]:
                dp[0][c] = 1
        mx = [0 for _ in range(L1)]
        mx[0] = max(dp[0])
        for r in range(1, L1):
            for c in range(1, L2):
                if A[r] == B[c]:
                    dp[r][c] = dp[r-1][c-1] + 1
            mx[r] = max(dp[r])
        return max(mx)
