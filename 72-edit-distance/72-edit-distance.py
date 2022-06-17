class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [n-j for j in range(n+1)]
        for i in reversed(range(m)):
            prev = dp[n]
            dp[n] += 1
            for j in reversed(range(n)): 
                curr = dp[j]
                if word1[i] == word2[j]: dp[j] = prev
                else: dp[j] = 1 + min(dp[j], dp[j+1], prev)
                prev = curr
        return dp[0]