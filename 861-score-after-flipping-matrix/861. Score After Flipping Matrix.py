class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Toggle rows to ensure the first column has all 1s
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1  # Toggle the entire row
        
        # Step 2: Toggle columns if there are more 0s than 1s in the column
        for j in range(1, n):
            zero_count = sum(grid[i][j] == 0 for i in range(m))
            if zero_count > m // 2:
                for i in range(m):
                    grid[i][j] ^= 1  # Toggle the entire column
        
        # Step 3: Calculate the final score
        score = 0
        for i in range(m):
            # Convert binary row to decimal and add to score
            row_value = int(''.join(map(str, grid[i])), 2)
            score += row_value
        
        return score
