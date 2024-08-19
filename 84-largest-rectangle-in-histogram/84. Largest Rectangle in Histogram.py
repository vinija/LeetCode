from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store indices of the histogram bars
        max_area = 0  # Variable to store the maximum area found
        index = 0  # Current index in the heights list
        
        while index < len(heights):
            # If the current bar is higher than the bar at stack's top or stack is empty
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top of the stack and calculate the area with the popped bar
                top_of_stack = stack.pop()
                height = heights[top_of_stack]
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, height * width)
        
        # Handle remaining bars in stack
        while stack:
            top_of_stack = stack.pop()
            height = heights[top_of_stack]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
