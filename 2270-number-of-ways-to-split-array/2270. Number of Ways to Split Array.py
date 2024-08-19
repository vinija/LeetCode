from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Step 1: Calculate total sum of the array
        left_sum = 0  # This will hold the sum of the left part
        valid_splits = 0  # Count of valid splits
        
        # Step 2: Iterate through all possible split points (except the last element)
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update the left sum
            right_sum = total_sum - left_sum  # Calculate right sum
            
            # Step 3: Check if the left part is greater than or equal to the right part
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits  # Step 4: Return the count of valid splits
