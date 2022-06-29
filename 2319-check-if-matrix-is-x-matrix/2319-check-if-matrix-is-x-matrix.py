class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
            m, n = len(grid), len(grid[0]) # problem states that m == n

            def isDiagonal(i,j):
                return i == j or (i + j + 1 == m)

            def isValid(i,j):
                return isDiagonal(i,j) == bool(grid[i][j]) # if it's diagonal, it's != 0; if it's not diagonal, it's 0

            return all(isValid(i,j) for i,j in product(range(m), range(n)))