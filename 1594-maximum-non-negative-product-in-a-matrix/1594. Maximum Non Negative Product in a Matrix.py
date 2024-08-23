from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Initialize dp tables for max and min products
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # Set initial value at the starting point
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Fill the first row
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
        
        # Fill the first column
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
        
        # Fill the rest of the dp tables
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
                    min_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
                else:
                    max_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
                    min_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
        
        max_product = max_dp[m - 1][n - 1]
        
        return max_product % MOD if max_product >= 0 else -1

# Example usage:
solution = Solution()
print(solution.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))  # Output: 8
print(solution.maxProductPath([[1, 3], [0, -4]]))  # Output: 0
print(solution.maxProductPath([[ -1, -2, -3], [ -2, -3, -3], [ -3, -3, -2]]))  # Output: -1
