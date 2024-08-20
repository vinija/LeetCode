class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dp(i, j):
            # Base case: if there is only one element, the player takes it
            if i == j:
                return nums[i]
            
            # Choose the leftmost element or the rightmost element
            # Subtract the value that the opponent will get after their optimal move
            pick_left = nums[i] - dp(i + 1, j)
            pick_right = nums[j] - dp(i, j - 1)
            
            # The player will choose the move that maximizes their score
            return max(pick_left, pick_right)
        
        # Check if the optimal score for player 1 is non-negative
        return dp(0, len(nums) - 1) >= 0
