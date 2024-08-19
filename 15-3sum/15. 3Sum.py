from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to facilitate the two-pointer approach and avoid duplicates
        nums.sort()
        result = []

        # Iterate through the array, considering each number as a potential start of a triplet
        for i in range(len(nums) - 2):
            # Skip duplicates for the current position to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find the other two numbers that sum to 0
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # If the sum is zero, we've found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                
                elif total < 0:
                    # If the sum is less than zero, move the left pointer to the right to increase the sum
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left to decrease the sum
                    right -= 1
        
        # Return the list of all unique triplets that sum to 0
        return result

        