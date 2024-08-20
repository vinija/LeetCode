class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Initialize the starting position
        row, col = 0, 0
        
        # Process each command
        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            elif command == "RIGHT":
                col += 1
        
        final_position = (row * n) + col
        return final_position