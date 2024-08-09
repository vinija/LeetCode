from collections import defaultdict
import heapq
from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        
        # Collect all elements of each diagonal
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heapq.heappush(diagonals[i - j], mat[i][j])
        
        # Put the sorted elements back into the matrix
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = heapq.heappop(diagonals[i - j])
        
        return mat
