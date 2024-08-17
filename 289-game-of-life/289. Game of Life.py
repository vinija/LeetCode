class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        liveCount = 0
        toChange = {}

        def valid(r, c):
            return (0 <= r < rows) and (0 <= c < cols)

        for r in range(rows):
            for c in range(cols):
                liveCount = 0
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if valid(newRow, newCol) and board[newRow][newCol] == 1:
                        liveCount += 1
                if board[r][c] == 1:
                    if liveCount < 2 or liveCount > 3:
                        toChange[(r, c)] = 0 
                else:
                    if liveCount == 3:
                        toChange[(r, c)] = 1  
        for (r, c), nextState in toChange.items():
            board[r][c] = nextState