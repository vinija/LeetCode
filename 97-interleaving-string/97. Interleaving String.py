class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check length first
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize the DP table
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # Base case: empty s1 and s2 match empty s3

        # Fill the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[len(s1)][len(s2)]
