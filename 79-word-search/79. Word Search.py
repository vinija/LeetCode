from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        self.rows, self.cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or board[r][c] != word[index]:
                return False

            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all possible directions (up, down, left, right)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # Backtrack: unmark the cell
            board[r][c] = temp
            return found

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:  # Optimization: only start DFS if first letter matches
                    if dfs(i, j, 0):
                        return True

        return False

# Example usage:
sol = Solution()
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
print(sol.exist(board, word))  # Output: True
