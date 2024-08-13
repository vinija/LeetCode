class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #initialize a 2D DP table
        dp = [[0] * (len(text2) +1) for _ in range(len(text1)+1)] 

        #Fill the DP table
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[len(text1)][len(text2)]