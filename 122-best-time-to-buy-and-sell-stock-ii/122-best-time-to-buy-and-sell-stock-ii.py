class Solution:
    #Rising Slope a<b<c: Here, the optimal solution is to buy stock at price "a", and sell it at price "c". This solution is respected by our algorithm, since we can see that our transactions would be: (b-a)+(c-b) = c-a
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for index in range(1,len(prices)):
            if prices[index] > prices[index-1] :
                maxProfit += prices[index] - prices[index-1]
        
        return maxProfit