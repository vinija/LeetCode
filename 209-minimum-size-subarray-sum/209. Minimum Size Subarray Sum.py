from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')  # Initialize to infinity to handle the case where no valid subarray is found
        current_sum = 0
        slow = 0

        for fast in range(len(nums)):
            current_sum += nums[fast]  # Expand the window by including nums[fast]

            # Contract the window from the left as long as the sum is greater than or equal to the target
            while current_sum >= target:
                min_len = min(min_len, fast - slow + 1)  # Update the minimum length
                current_sum -= nums[slow]  # Contract the window
                slow += 1

        # Return 0 if no valid subarray is found, otherwise return the minimum length found
        return 0 if min_len == float('inf') else min_len
