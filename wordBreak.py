class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)
        # intialize all data structure
        # dp[i] from i to end of the string can be sigmented by wordDict
        # initializing dp: len(s) + 1 where dp[-1] = True, others False
        dp = [False for _ in range(L+1)]
        dp[-1] = True
        # words: dictionary where key = starting character and value = list of word 
        words = defaultdict(list)
        for word in wordDict:
            words[word[0]].append(word)

        for i in range(L - 1, -1, -1):
            for word in words[s[i]]:
                L2 = len(word)
                # dp[i] = dp[i:j] in wordDict && dp[j:]
                if L2 <= L - i and word == s[i: i + L2]:
                    dp[i] = dp[i] or dp[L2 + i]
        
        return dp[0]
