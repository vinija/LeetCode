from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        slow = 0
        fast = len(height) - 1
        maxArea = 0

        while slow < fast:
            # Calculate the current area
            currHeight = min(height[slow], height[fast])
            currArea = (fast - slow) * currHeight
            # Update maxArea if the current area is larger
            maxArea = max(maxArea, currArea)
            
            # Move the pointer with the smaller height
            if height[slow] < height[fast]:
                slow += 1
            else:
                fast -= 1

        return maxArea
