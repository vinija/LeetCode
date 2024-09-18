class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        row = len(matrix)
        col = len(matrix[0])

        # Use two flags to check if first row and first column need to be set to zero
        first_row_zero = False
        first_col_zero = False

        # Determine if the first row has any zeros
        for c in range(col):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # Determine if the first column has any zeros
        for r in range(row):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # Use first row and column to mark zero rows and columns
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Mark the row
                    matrix[0][c] = 0  # Mark the column

        # Zero out cells based on marks in the first row and first column
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out the first row if necessary
        if first_row_zero:
            for c in range(col):
                matrix[0][c] = 0

        # Zero out the first column if necessary
        if first_col_zero:
            for r in range(row):
                matrix[r][0] = 0
