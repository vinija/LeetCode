class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Extract the column (letter) and row (number) from the coordinates
        column = coordinates[0]
        row = coordinates[1]
        
        # Convert the column letter to a number (e.g., 'a' -> 1, 'b' -> 2, etc.)
        column_number = ord(column) - ord('a') + 1
        
        # Convert the row to an integer
        row_number = int(row)
        
        # A square is white if the sum of the column and row numbers is odd
        return (column_number + row_number) % 2 == 1
