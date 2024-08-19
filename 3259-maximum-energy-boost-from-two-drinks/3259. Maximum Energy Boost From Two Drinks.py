from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        
        # Initialize dp arrays
        dpA = [0] * n
        dpB = [0] * n
        
        # Initial values for the first hour
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        
        # Fill dp arrays for each hour
        for i in range(1, n):
            dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-1])
            dpB[i] = max(dpB[i-1] + energyDrinkB[i], dpA[i-1])
        
        # The result is the maximum value between the last elements of dpA and dpB
        return max(dpA[-1], dpB[-1])

# Example usage:
sol = Solution()
print(sol.maxEnergyBoost([1,3,1], [3,1,1]))  # Output: 5
print(sol.maxEnergyBoost([4,1,1], [1,1,3]))  # Output: 7
