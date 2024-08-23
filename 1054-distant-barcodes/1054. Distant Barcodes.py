from typing import List
import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Step 1: Count the frequency of each barcode
        freq = Counter(barcodes)
        
        # Step 2: Create a max-heap based on frequencies
        # Python's heapq is a min-heap, so we use negative frequencies
        max_heap = [(-count, barcode) for barcode, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_count, prev_barcode = 0, None
        
        # Step 3: Rearrange the barcodes
        while max_heap:
            count, barcode = heapq.heappop(max_heap)
            # Add the current barcode to the result
            result.append(barcode)
            
            # If there's a previously used barcode, push it back into the heap
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_barcode))
            
            # Update prev_count and prev_barcode for the next iteration
            prev_count, prev_barcode = count + 1, barcode  # +1 because count is negative
        
        return result

# Example usage:
solution = Solution()
print(solution.rearrangeBarcodes([1, 1, 1, 2, 2, 3]))  # Output: [1, 2, 1, 3, 1, 2] or other valid arrangement
print(solution.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))  # Output: [1, 2, 1, 3, 1, 2, 1, 3] or other valid arrangement
