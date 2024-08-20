class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # dp[i][M] will store the maximum number of stones Alice can get starting from the ith pile with M
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # suffix_sum[i] will store the total number of stones from the ith pile to the end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        # Fill suffix_sum from the end to the beginning
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # Fill the dp table from the end to the beginning
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                # If we can take all the remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix_sum[i]
                else:
                    # Consider taking X piles where 1 <= X <= 2M
                    for X in range(1, 2 * M + 1):
                        dp[i][M] = max(dp[i][M], suffix_sum[i] - dp[i + X][max(M, X)])
        
        # The answer is the maximum stones Alice can get starting from the first pile with M = 1
        return dp[0][1]

# Example usage:
# piles = [2, 7, 9, 4, 4]
# solution = Solution()
# print(solution.stoneGameII(piles))  # Output: 10
