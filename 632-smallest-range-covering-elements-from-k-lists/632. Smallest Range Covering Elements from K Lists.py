import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Using a min-heap to efficiently extract the smallest item among the current heads of the lists
        min_heap = []
        current_max = float('-inf')

        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        # Initialize smallestRange with a range that could feasibly be the largest based on inputs
        smallest_range = [0, float('inf')]

        # Process the heap until we cannot form a complete range
        while min_heap:
            min_val, i, j = heapq.heappop(min_heap)
            # Update the smallest range if the new range is smaller
            if current_max - min_val < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_val, current_max]

            # Move to the next element in the list from which the element was taken
            if j + 1 < len(nums[i]):
                next_val = nums[i][j + 1]
                heapq.heappush(min_heap, (next_val, i, j + 1))
                current_max = max(current_max, next_val)
            else:
                # If we run out of elements in any list, we stop
                break

        return smallest_range

# Example usage:
sol = Solution()
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(sol.smallestRange(nums))  # Output should be: [20, 24]
