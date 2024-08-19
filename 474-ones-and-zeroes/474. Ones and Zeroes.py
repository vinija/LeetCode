class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D DP array with dimensions (m+1) x (n+1)
        # dp[i][j] represents the maximum size of the subset with at most i 0's and j 1's
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate over each string in strs
        for s in strs:
            # Count the number of 0's and 1's in the current string
            zeros = s.count('0')
            ones = s.count('1')

            # Update the DP array from bottom-right to top-left
            # We iterate backwards to avoid overwriting the dp values we still need to use
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # The state transition: either include the current string or exclude it
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        # The answer will be in dp[m][n], the maximum subset size with at most m 0's and n 1's
        return dp[m][n]
