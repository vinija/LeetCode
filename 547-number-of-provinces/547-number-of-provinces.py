# time: O(n^2)
# space: O(n) to store visit list

class Solution:
    def dfs(self, r, grid, visited):
        visited.append(r)
        for j in range(len(grid)):
            if grid[r][j] == 1 and j not in visited:
                self.dfs(j, grid, visited)

    def findCircleNum(self, M) -> int:

        visited = []
        count = 0
        for row in range(len(M)):
            if row not in visited:
                self.dfs(row, M, visited)
                count += 1
        return count