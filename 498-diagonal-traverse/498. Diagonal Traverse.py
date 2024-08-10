from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        # Populate the diagonals dictionary
        for i in range(m):
            for j in range(n):
                # Append elements to the corresponding diagonal group
                diagonals[i + j].append(mat[i][j])
        
        result = []
        
        # Traverse diagonals in zigzag order
        for k in range(m + n - 1):
            if k % 2 == 0:
                # For even sum of indices, reverse the diagonal before adding
                result.extend(diagonals[k][::-1])
            else:
                # For odd sum of indices, add the diagonal as is
                result.extend(diagonals[k])
        
        return result
