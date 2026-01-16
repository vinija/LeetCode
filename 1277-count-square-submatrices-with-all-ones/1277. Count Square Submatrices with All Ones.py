from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Counts the total number of square submatrices with all ones.

        Args:
            matrix (List[List[int]]): A 2D binary matrix containing only 0s and 1s.

        Returns:
            int: Total number of square submatrices with all ones.

        Raises:
            ValueError: If the input matrix is empty or malformed.
        """

        # -----------------------------
        # Input validation
        # -----------------------------
        if matrix is None:
            raise ValueError("Input matrix cannot be None.")

        if not matrix or not matrix[0]:
            raise ValueError("Input matrix must have at least one row and one column.")

        rows: int = len(matrix)
        cols: int = len(matrix[0])

        for row in matrix:
            if len(row) != cols:
                raise ValueError("All rows in the matrix must have the same length.")
            for val in row:
                if val not in (0, 1):
                    raise ValueError("Matrix values must be either 0 or 1.")

        # -----------------------------
        # Dynamic Programming table
        # dp[i][j] = size of largest square
        # ending at (i, j)
        # -----------------------------
        dp: List[List[int]] = [[0] * cols for _ in range(rows)]
        total_squares: int = 0

        # -----------------------------
        # DP computation
        # -----------------------------
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # First row or first column can only form squares of size 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i - 1][j],      # top
                            dp[i][j - 1],      # left
                            dp[i - 1][j - 1]   # top-left
                        )

                    # Each dp[i][j] contributes dp[i][j] squares
                    total_squares += dp[i][j]

        return total_squares


# -----------------------------
# Time and Space Complexity
# -----------------------------
# Time Complexity:
# O(m × n), where m = number of rows and n = number of columns.
# Each cell is processed exactly once.

# Space Complexity:
# O(m × n) for the DP table.
# This can be optimized to O(n) using a rolling array, but clarity is preferred.


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    matrix1 = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(solution.countSquares(matrix1))  # Expected output: 15

    # Test Case 2
    matrix2 = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(solution.countSquares(matrix2))  # Expected output: 7
