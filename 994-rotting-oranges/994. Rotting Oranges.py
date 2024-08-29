from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh_count = 0

        #Step 1: init the queue with rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: #rotten
                    queue.append((r,c))
                elif grid[r][c] == 1: #fresh
                    fresh_count +=1
        
        if fresh_count == 0:
            return 0

        #Step 2: BFS to rot the fresh oranges
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        min_passed = 0

        while fresh_count > 0 and queue:
            min_passed +=1

            for _ in range(len(queue)):
                x, y = queue.popleft()

                #check all directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    #check if new position w/in bounds and if fresh orange here
                    if 0 <= nx < rows and 0<= ny < cols and grid[nx][ny] == 1:
                        #rot the orange
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx,ny))
                




        #Step 3: return the time
        return min_passed if fresh_count == 0 else -1
        