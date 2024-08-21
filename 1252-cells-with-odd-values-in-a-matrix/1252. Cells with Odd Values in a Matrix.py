class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize row and column counters
        row_count = [0] * m
        col_count = [0] * n
        
        # Increment the row and column counters based on the indices
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        # Count the number of cells with odd values
        odd_count = 0
        for i in range(m):
            for j in range(n):
                # The value at cell (i, j) is odd if the sum of row_count[i] and col_count[j] is odd
                if (row_count[i] + col_count[j]) % 2 != 0:
                    odd_count += 1
        
        return odd_count

        