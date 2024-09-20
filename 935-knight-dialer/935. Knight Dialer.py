class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Knight's possible moves for each number
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # DP table to store the number of ways to reach each number
        dp = [1] * 10  # Base case: 1 way to reach each number at step 1

        # Iterate for every step from 2 to n
        for i in range(1, n):
            new_dp = [0] * 10
            for num in range(10):
                for move in moves[num]:
                    new_dp[num] = (new_dp[num] + dp[move]) % MOD
            dp = new_dp  # Move to the next step
        
        return sum(dp) % MOD
