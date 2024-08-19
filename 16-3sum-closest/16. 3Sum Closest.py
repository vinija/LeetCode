from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to apply the two-pointer technique
        nums.sort()
        
        # Initialize the closest sum with a very large value
        closest_sum = float('inf')
        
        # Iterate through the array, fixing one element at a time
        for i in range(len(nums) - 2):
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                # Calculate the current sum of the triplet
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is exactly equal to the target, return it
                if current_sum == target:
                    return current_sum
                
                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the left pointer to the right if the current sum is less than the target
                if current_sum < target:
                    left += 1
                # Move the right pointer to the left if the current sum is greater than the target
                else:
                    right -= 1
        
        # Return the closest sum found
        return closest_sum
