class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        # Initialize the board, n = 3 in this problem.
        n = 3
        board = [[0] * n for _ in range(n)]
        
        # Check if any of 4 winning conditions to see if the current player has won.
        def checkRow(row, player_id):
            for col in range(n):
                if board[row][col] != player_id:
                    return False
            return True
        
        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True
        
        def checkDiagonal(player_id):
            for row in range(n):
                if board[row][row] != player_id:
                    return False
            return True
        
        def checkAntiDiagonal(player_id):
            for row in range(n):
                if board[row][n - 1 - row] != player_id:
                    return False
            return True
        
        # Start with player_1.
        player = 1

        for move in moves:
            # extract 
            row, col = move
            board[row][col] = player
            
            # If any of the winning conditions is met, return the current player's id.
            if checkRow(row, player) or checkCol(col, player) or \
            (row == col and checkDiagonal(player)) or \
            (row + col == n - 1 and checkAntiDiagonal(player)):
                return 'A' if player == 1 else 'B'
            
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if
        # the grid is full or not. If so, the game ends with draw, otherwise pending.    
        return "Draw" if len(moves) == n * n else "Pending"