class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1
        
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    special_count += 1
        
        return special_count