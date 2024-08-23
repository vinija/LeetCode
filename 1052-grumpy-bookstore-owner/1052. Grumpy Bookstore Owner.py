from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Initial satisfied customers count
        satisfied_customers = 0
        # Additional satisfied customers due to using the technique
        additional_satisfied = 0
        # Maximum additional satisfied customers we can get
        max_additional_satisfied = 0

        n = len(customers)

        # Calculate the initial satisfied customers and the first window's additional satisfied
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
            else:
                if i < minutes:
                    additional_satisfied += customers[i]

        # Set max_additional_satisfied to the first window's additional satisfied customers
        max_additional_satisfied = additional_satisfied

        # Sliding window to find the optimal additional satisfied customers
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]

            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)

        # The total maximum satisfied customers is the sum of initially satisfied customers
        # and the maximum additional satisfied customers from the optimal window
        return satisfied_customers + max_additional_satisfied

# Example usage:
solution = Solution()
print(solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))  # Output: 16
print(solution.maxSatisfied([1], [0], 1))  # Output: 1
