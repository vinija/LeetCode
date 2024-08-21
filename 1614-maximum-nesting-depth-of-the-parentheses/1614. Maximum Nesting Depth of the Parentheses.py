class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0  # To keep track of the current depth
        max_depth = 0  # To keep track of the maximum depth encountered

        # Iterate through each character in the string
        for char in s:
            if char == '(':
                current_depth += 1  # Increase depth for an opening parenthesis
                max_depth = max(max_depth, current_depth)  # Update max depth if needed
            elif char == ')':
                current_depth -= 1  # Decrease depth for a closing parenthesis
        
        return max_depth  # Return the maximum depth encountered
