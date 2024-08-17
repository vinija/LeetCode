from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in non-decreasing order
        citations.sort()
        
        n = len(citations)
        
        # Traverse the sorted list and find the h-index
        for i in range(n):
            # The h-index is where citations[i] >= n - i
            if citations[i] >= n - i:
                return n - i
        
        # If no valid h-index is found, return 0
        return 0
