class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i][j] will store the number of palindromic subsequences in the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: Single characters are palindromic subsequences of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill dp table
        for length in range(2, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    
                    # Find the first and last occurrence of s[i] in s[i+1:j]
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while low <= high and s[high] != s[j]:
                        high -= 1
                    
                    if low > high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                
                # Ensure the result is within the modulo constraint
                dp[i][j] = (dp[i][j] + MOD) % MOD
        
        # The answer is the number of palindromic subsequences in the whole string
        return dp[0][n - 1]
