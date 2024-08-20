class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        original_rows = len(mat)
        original_cols = len(mat[0])

        #check if reshape is possible
        if original_rows * original_cols != r * c:
            return mat
        
        flat_list = []
        for row in mat:
            for num in row:
                flat_list.append(num)
        
        reshaped_matrix = []

        for i in range(r):
            reshaped_matrix.append(flat_list[i * c:(i + 1) * c])

        return reshaped_matrix