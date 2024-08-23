from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        i, j = 0, 0 # init row and col pointers

        while i < m and j < n:
            #determine the min value to fill in the current cell
            value = min(rowSum[i], colSum[j])
            matrix[i][j] = value

            #update rowSum and colSum with assigned value
            rowSum[i] -= value
            colSum[j] -= value

            #move to the next row or col based on which sum reaches zero
            if rowSum[i] == 0:
                i += 1 #move to the next row
            if colSum[j] == 0:
                j+= 1
        return matrix
        