from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        # Populate the diagonals dictionary
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                diagonals[i + j].append(num)
        
        # Sort the keys to traverse diagonals in order
        sorted_keys = sorted(diagonals.keys())
        
        result = []
        for key in sorted_keys:
            # Reverse the list to have higher row index first
            result.extend(diagonals[key][::-1])
        
        return result
