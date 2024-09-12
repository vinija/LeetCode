class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        # Directions for 8 possible moves (including diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        n = len(grid)
        queue = deque([(0,0,1)])
        grid[0][0] = 1

        while queue:
            r,c,dist = queue.popleft()

            #exit condition
            if r == n - 1 and c == n - 1:
                return dist
            
            #explore all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c+dc

                #mark as visited
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr,nc, dist+1))
                    grid[nr][nc] = 1
        return -1
            


        
