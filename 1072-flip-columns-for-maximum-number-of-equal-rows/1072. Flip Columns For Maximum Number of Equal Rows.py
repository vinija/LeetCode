from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)

        for row in matrix:

            #Normalize the row pattern
            normalized = tuple(row[i] if row[0] == 0 else 1 - row[i] for i in range(len(row)))
            pattern_count[normalized] += 1
        
        return max(pattern_count.values())
        