from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                #If current number is negative, all numbers in this row to the right are negative
                count += n - col
                row -= 1 # move up to the previous row
            else:
                col += 1 # move right to find a negative number

        return count

        