
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if (r == c) or (r+c == row-1):
                    if grid[r][c] == 0:
                        return False
                if (r != c ) and (r+c != row-1 ):
                    if grid[r][c] != 0:
                        return False
        return True