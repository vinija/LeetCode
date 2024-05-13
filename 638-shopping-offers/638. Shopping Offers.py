class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo = {}

        def dfs(currentNeeds):

            needsTuple = tuple(currentNeeds)
            if needsTuple in memo:
                return memo[needsTuple]
            
            minCost = sum(currentNeeds[i] * price[i] for i in range(len(price)))

            for offer in special:
                newNeeds = currentNeeds [:]

                for i in range(len(price)):
                    if offer[i] > newNeeds[i]:
                        break
                else:
                    for i in range(len(price)):
                        newNeeds[i] -= offer[i]
                    offerCost = offer[-1] + dfs(newNeeds)
                    minCost = min(minCost, offerCost)
            memo[needsTuple] = minCost
            return minCost
        return dfs(needs)