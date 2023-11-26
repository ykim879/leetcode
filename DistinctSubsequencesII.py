class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        last = {}
        for i,v in enumerate(s):
            res = 2 * dp[i]
            if v in last:
                res -= dp[last[v]]
            dp[i+1] = res
            last[v] = i # addition to added 
        return (dp[-1] - 1) %(10 ** 9 + 7) #-1 is empty string
