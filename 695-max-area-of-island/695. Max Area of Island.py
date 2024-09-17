from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        
        # Helper function for DFS to calculate the area of an island
        def dfs(r: int, c: int) -> int:
            # If the current position is out of bounds or it's water (0), return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            # Mark the current land cell as visited by setting it to 0 (water)
            grid[r][c] = 0
            # Initialize the area of this part of the island as 1 (the current cell)
            area = 1
            # Explore the four possible directions (up, down, left, right)
            area += dfs(r + 1, c)  # Down
            area += dfs(r - 1, c)  # Up
            area += dfs(r, c + 1)  # Right
            area += dfs(r, c - 1)  # Left
            # Return the total area for this connected island
            return area
        
        # Initialize a variable to keep track of the maximum island area found
        max_area = 0
        
        # Loop through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land (1), start a DFS to calculate the area of the island
                if grid[r][c] == 1:
                    # Use DFS to compute the area of the island
                    max_area = max(max_area, dfs(r, c))
        
        # Return the largest area of any island found
        return max_area
