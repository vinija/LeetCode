from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the global min and max using the first array
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        max_distance = 0
        
        # Iterate through the rest of the arrays
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate possible maximum distances using the current array
            max_distance = max(max_distance, abs(current_max - global_min), abs(global_max - current_min))
            
            # Update global min and max
            global_min = min(global_min, current_min)
            global_max = max(global_max, current_max)
        
        return max_distance

# Example usage:
solution = Solution()
print(solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))  # Output: 4
print(solution.maxDistance([[1], [1]]))  # Output: 0
