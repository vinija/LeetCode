from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:  # Check if the matrix is empty or has no columns
            return 0  # Return 0 if the matrix is empty
        
        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns in the matrix
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]  # Initialize memoization table with -1
        
        # Directions for moving right, down, left, and up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c):
            if memo[r][c] != -1:  # If the path length from this cell is already computed
                return memo[r][c]  # Return the cached value
            
            max_len = 1  # The minimum path length is 1 (the cell itself)
            for dr, dc in directions:  # Explore all four possible directions
                nr, nc = r + dr, c + dc  # Calculate the new row and column indices
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:  # Check if the move is valid
                    max_len = max(max_len, 1 + dfs(nr, nc))  # Recursively compute the path length from the new cell
            
            memo[r][c] = max_len  # Store the computed maximum path length in the memoization table
            return max_len  # Return the maximum path length from this cell
        
        longest_path = 0  # Initialize the variable to track the longest path found
        for r in range(rows):  # Iterate over each row in the matrix
            for c in range(cols):  # Iterate over each column in the matrix
                longest_path = max(longest_path, dfs(r, c))  # Update the longest path found with the result from dfs
        
        return longest_path  # Return the length of the longest increasing path found
