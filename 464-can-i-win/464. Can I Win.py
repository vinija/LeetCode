class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all numbers is less than the desired total, no one can win
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False
        
        # Dictionary to store the results of subproblems (memoization)
        memo = {}
        
        # Helper function to check if the current player can win
        def can_win(used_numbers, current_total):
            # If this state has been computed before, return the stored result
            if used_numbers in memo:
                return memo[used_numbers]
            
            # Try every possible number that hasn't been used yet
            for i in range(1, maxChoosableInteger + 1):
                current_mask = 1 << i
                if used_numbers & current_mask == 0:  # If the number i hasn't been used
                    # If choosing i reaches or exceeds the desired total, or if the opponent loses in the next turn, return True
                    if current_total + i >= desiredTotal or not can_win(used_numbers | current_mask, current_total + i):
                        memo[used_numbers] = True
                        return True
            
            # If none of the choices lead to a win, return False
            memo[used_numbers] = False
            return False
        
        # Initial call with no numbers used and a current total of 0
        return can_win(0, 0)
