class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #bottoms up
        dp = [0] + [float("inf")] * amount
        
        for coin in coins:
            for index in range(coin, amount+1):
                dp[index] = min(dp[index], dp[index-coin]+1)
        
        print(dp)
        
        return dp[-1] if dp[-1] != float("inf") else -1