class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Step 1: Calculate the total length of all matchsticks
        total_length = sum(matchsticks)
        
        # Step 2: Check if the total length is divisible by 4 (since a square has 4 equal sides)
        if total_length % 4 != 0:
            return False
        
        # Step 3: The side length of the square
        side_length = total_length // 4
        
        # Step 4: Sort the matchsticks in descending order to try larger sticks first (optimization)
        matchsticks.sort(reverse=True)
        
        # Step 5: Initialize an array to hold the length of each side
        sides = [0] * 4
        
        # Step 6: Backtracking function to try to form the square
        def backtrack(index):
            # If we've placed all matchsticks, check if all sides are equal to the target side length
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length
            
            # Try to place the current matchstick in each of the 4 sides
            for i in range(4):
                # Check if the matchstick can be placed on the i-th side
                if sides[i] + matchsticks[index] <= side_length:
                    # Place the matchstick on the i-th side
                    sides[i] += matchsticks[index]
                    
                    # Recurse to place the next matchstick
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack if placing the matchstick doesn't lead to a solution
                    sides[i] -= matchsticks[index]
                
                # Optimization: if the current side length is 0 (no matchsticks placed yet), break to avoid redundant work
                if sides[i] == 0:
                    break
            
            # If no placement leads to a solution, return False
            return False
        
        # Start the backtracking process from the first matchstick
        return backtrack(0)
