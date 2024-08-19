class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Step 1: Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Step 2: Initialize a list of empty strings for each row
        rows = [''] * numRows
        cur_row = 0  # Start at the first row
        going_down = False  # This flag helps in changing direction
        
        # Step 3: Iterate over the string, placing characters in the appropriate row
        for char in s:
            rows[cur_row] += char  # Place the character in the current row
            # If we are at the top or bottom row, we change direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down  # Toggle direction
            # Move up or down based on the current direction
            cur_row += 1 if going_down else -1
        
        # Step 4: Join all rows to form the final zigzag string
        return ''.join(rows)
