class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: If the string starts with '0', it can't be decoded
        if not s or s[0] == '0':
            return 0
        
        # DP array where dp[i] represents the number of ways to decode up to the i-th character
        n = len(s)
        dp = [0] * (n + 1)
        
        # Base cases:
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode a string of length 1 if it's not '0'

        # Fill the DP array
        for i in range(2, n + 1):
            # Check if the single character at position i-1 is valid (i.e., between '1' and '9')
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the two characters at position i-2 and i-1 form a valid number (i.e., between '10' and '26')
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
