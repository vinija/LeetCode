class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        transposed_matrix = [[0] * rows for _ in range(cols)]

        #fill the transposed matrix
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix
        