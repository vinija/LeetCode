from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If the starting point or the ending point is an obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Initialize the DP table
        dp = [[0] * n for _ in range(m)]
        
        # Start point
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        
        # The result is in the bottom-right corner
        return dp[-1][-1]
