class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Memoization dictionary to store the results for different needs
        memo = {}
        
        def dfs(current_needs):
            # Convert current needs to a tuple to use as a key in memoization dictionary
            needs_tuple = tuple(current_needs)
            
            # If already computed, return the stored result
            if needs_tuple in memo:
                return memo[needs_tuple]
            
            # Calculate the cost without any special offers
            total_cost = sum(current_needs[i] * price[i] for i in range(len(needs)))
            
            # Try to apply each special offer
            for offer in special:
                new_needs = []
                for i in range(len(current_needs)):
                    if current_needs[i] < offer[i]:  # Cannot use this offer
                        break
                    new_needs.append(current_needs[i] - offer[i])
                else:  # If we didn't break, the offer is valid
                    total_cost = min(total_cost, offer[-1] + dfs(new_needs))
            
            # Store the result in memo dictionary
            memo[needs_tuple] = total_cost
            return total_cost
        
        # Start the recursive process
        return dfs(needs)
