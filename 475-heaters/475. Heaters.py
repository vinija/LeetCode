class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort both houses and heaters
        houses.sort()
        heaters.sort()
        
        # Function to find the nearest heater to a house using binary search
        def find_nearest_heater(house):
            left, right = 0, len(heaters) - 1
            
            # Binary search to find the closest heater
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            
            # Get the minimum distance between the house and the nearest heater
            nearest_dist = abs(heaters[left] - house)
            if left > 0:
                nearest_dist = min(nearest_dist, abs(heaters[left - 1] - house))
            
            return nearest_dist

        # Initialize the minimum radius
        min_radius = 0
        
        # For each house, find the minimum distance to the nearest heater
        for house in houses:
            min_radius = max(min_radius, find_nearest_heater(house))
        
        # Return the minimum radius required to cover all houses
        return min_radius
