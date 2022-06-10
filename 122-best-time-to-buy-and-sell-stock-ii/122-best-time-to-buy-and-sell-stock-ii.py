class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for index in range(1,len(prices)):
            if prices[index] > prices[index-1] :
                maxProfit += prices[index] - prices[index-1]
        
        return maxProfit