from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Initializes the NumMatrix object with the integer matrix.
        Preprocesses the matrix to compute prefix sums for efficient sumRegion queries.
        """
        if not matrix or not matrix[0]:
            # Handle empty matrix case
            self.prefix_sum = [[0]]
            return
        
        m, n = len(matrix), len(matrix[0])
        # Initialize prefix_sum matrix with dimensions (m+1) x (n+1) filled with 0
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Compute prefix sums
        for i in range(1, m + 1):
            row_sum = 0  # Cumulative sum for the current row
            for j in range(1, n + 1):
                row_sum += matrix[i-1][j-1]  # Sum of the current row up to column j
                # prefix_sum[i][j] = current element + sum above + sum to the left - sum diagonally above-left
                self.prefix_sum[i][j] = row_sum + self.prefix_sum[i-1][j]
        
        # Debug: Print the prefix_sum matrix
        # for row in self.prefix_sum:
        #     print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of the elements within the rectangle defined by its upper left corner (row1, col1)
        and lower right corner (row2, col2).
        """
        # Since prefix_sum has an extra row and column at the beginning, we add 1 to indices
        sum_total = self.prefix_sum[row2 + 1][col2 + 1]
        sum_above = self.prefix_sum[row1][col2 + 1]
        sum_left = self.prefix_sum[row2 + 1][col1]
        sum_overlap = self.prefix_sum[row1][col1]
        
        # Calculate the sum using inclusion-exclusion principle
        region_sum = sum_total - sum_above - sum_left + sum_overlap
        return region_sum

# Example Usage:
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
    print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
    print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
