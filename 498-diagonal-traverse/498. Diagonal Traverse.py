from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 means moving up-right, -1 means moving down-left

        for _ in range(m * n):
            result.append(mat[row][col])

            # Moving in the up-right direction
            if direction == 1:
                if col == n - 1:  # Hit the right boundary
                    row += 1
                    direction = -1
                elif row == 0:  # Hit the top boundary
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1

            # Moving in the down-left direction
            else:
                if row == m - 1:  # Hit the bottom boundary
                    col += 1
                    direction = 1
                elif col == 0:  # Hit the left boundary
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result
