class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # init the result list with the starting position
        result = [[rStart, cStart]]

        # define the direction in order, east, south, west, north
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]

        #steps to take in current direction
        steps = 1 # Initially, we move one step in the first direction

        #While we havent visted all cells in the grid
        while len(result) < rows * cols:
            for i in range(4):
                dx, dy = directions[i]

                for _ in range(steps):
                    rStart += dx
                    cStart += dy

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart,cStart])
                
                if i == 1 or i == 3:
                    steps += 1
        return result