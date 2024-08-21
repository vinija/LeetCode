class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        # Iterate over the length of the substring
        for length in range(1, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # Start with the worst case scenario
                
                # Base case: one character
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + 1  # Worst case: print s[i] separately
                    
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - (1 if s[k] == s[j] else 0))
        
        return dp[0][n-1]
