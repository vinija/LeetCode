from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to determine if mid is a feasible capacity
        def canShipWithCapacity(capacity):
            current_sum = 0
            required_days = 1  # Start with one day by default
            for weight in weights:
                # Check if adding this package would exceed capacity
                if current_sum + weight > capacity:
                    # Need a new day, reset current_sum
                    required_days += 1
                    current_sum = weight
                    # If number of days exceeds the allowed days, return False
                    if required_days > days:
                        return False
                else:
                    # Keep adding weight to the current day
                    current_sum += weight
            return True
        
        # Define the binary search bounds
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShipWithCapacity(mid):
                right = mid  # Try a smaller capacity
            else:
                left = mid + 1  # Increase the capacity

        return left

# Example usage:
sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15
print(sol.shipWithinDays([3,2,2,4,1,4], 3))  # Output: 6
