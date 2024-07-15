from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append(''.join('Q' if i == row else '.' for i in range(n)))
            return board
        
        def backtrack(row):
            if row == n:
                solution = create_board(queens)
                results.append(solution)
                return
            for col in range(n):
                if col in columns or (row - col) in main_diag or (row + col) in anti_diag:
                    continue
                queens.append(col)
                columns.add(col)
                main_diag.add(row - col)
                anti_diag.add(row + col)
                
                backtrack(row + 1)
                
                queens.pop()
                columns.remove(col)
                main_diag.remove(row - col)
                anti_diag.remove(row + col)
        
        results = []
        queens = []  # This list holds the column index of the placed queens
        columns = set()  # Tracks occupied columns
        main_diag = set()  # Tracks occupied main diagonals
        anti_diag = set()  # Tracks occupied anti-diagonals
        backtrack(0)
        return results

        