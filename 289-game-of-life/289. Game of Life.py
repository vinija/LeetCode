class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #get dimensions of the board
        rowLen = len(board[0])
        colLen = len(board)

        # Create a copy of the board to store the updated states
        ans = [[-1 for x in range(rowLen)] for y in range(colLen)]

        # Helper function to check if a cell is within the board's bounds
        def inBound(i, j):
            return (0 <= i < colLen) and (0 <= j < rowLen)
        
        for i in range(colLen):
            for j in range(rowLen):
                count = 0

                # Check the eight possible neighbors
                for ii, jj in [
                    (i, j+1), (i, j-1), (i-1, j), (i+1, j), 
                    (i-1, j+1), (i+1, j-1), (i+1, j+1), (i-1, j-1)
                ]:
                    if inBound(ii, jj):  # Ensure the neighbor is within bounds
                        count += board[ii][jj]  # Count live neighbors
                                # Apply the Game of Life rules to determine the next state of the cell
                if count < 2:
                    ans[i][j] = 0  # Rule 1: Underpopulation
                elif board[i][j] == 1 and (count == 2 or count == 3):
                    ans[i][j] = 1  # Rule 2: Survival
                elif board[i][j] == 1 and count > 3:
                    ans[i][j] = 0  # Rule 3: Overpopulation
                elif board[i][j] == 0 and count == 3:
                    ans[i][j] = 1  # Rule 4: Reproduction
                else:
                    ans[i][j] = board[i][j]  # Keep the state if no rule applies
        board[:] = ans

        return board
                



