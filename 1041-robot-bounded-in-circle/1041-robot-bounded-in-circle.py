class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north, east, south, west
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        x, y, direction = 0, 0, 0 # north
        
        for i in instructions:
            if i == 'G':
                x += move[direction][0]
                y += move[direction][1]
            
            if i == 'L':
                direction = (direction + 1) % 4
            
            if i == 'R':
                direction = (direction + 4 - 1) % 4
            
        return (x == 0 and y == 0) or direction != 0