class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]
        #trick question as it will take the same time going down or going left first
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]