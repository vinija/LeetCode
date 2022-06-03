class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1
        
        #make the move
        self.rows[row] += p
        self.cols[col] += p
        
        if row == col:
            self.diagonal += p
        
        if row + col == self.n - 1:
            self.anti_diagonal += p
        
        #winning condition
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        
        return 0
      


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)