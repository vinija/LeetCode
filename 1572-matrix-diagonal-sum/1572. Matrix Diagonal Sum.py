class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total_sum = 0

        n = len(mat) # matrix is n x n

        #Iterate through each row in the matrix
        for i in range(n):
            total_sum += mat[i][i]

            if i != n -1 - i:
                total_sum += mat[i][n - 1 - i]

        return total_sum