# To reduce the conditional complexity in the for-loop, I just separated this into 3 steps:

# Progress along the first col all the way right
# Progress along the first row all the way down
# Process all other cells (Those with both left and top parents)
# O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: 
            return 0
        
        for col in range(1, len(grid)): 
            grid[col][0] += grid[col - 1][0]
        
        for row in range(1, len(grid[0])):
            grid[0][row] += grid[0][row - 1]
        
        for col in range(1, len(grid)):
            for row in range(1, len(grid[0])):
                grid[col][row] += min(grid[col - 1][row], grid[col][row - 1])
        
        return grid[-1][-1]