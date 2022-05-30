class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = set(), deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    fresh.add((row,col))
                elif grid[row][col] == 2:
                    rotten.append((row,col))
        minutes = 0
        
        while fresh and rotten:
            minutes +=1
            
            for rot in range(len(rotten)):
                
                row,col = rotten.popleft()
                
                for direction in ((row-1,col), (row+1,col), (row, col-1), (row,col+1)):
                    if direction in fresh:
                        
                        fresh.remove(direction)
                        rotten.append(direction)
        
        return -1 if fresh else minutes