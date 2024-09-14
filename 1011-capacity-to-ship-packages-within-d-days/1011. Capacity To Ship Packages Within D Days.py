from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #Helper function to determine how many days are needed to ship all packages
        def canShipInDays(capacity: int) -> bool:
            current_weight = 0
            days_needed = 1 #Start with the first day

            for weight in weights:
                #If added weight exceeds capacity, need more days
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0
                current_weight += weight

                #if exceed num of days, return false
                if days_needed > days:
                    return False
            return True
        
        #Binary search possible ship capacities
        left = max(weights) #least possible capacity
        right = sum(weights) #max capacity

        while left < right:
            mid = (left + right) // 2
            if canShipInDays(mid):
                right = mid
            else:
                left = mid + 1
        return left
