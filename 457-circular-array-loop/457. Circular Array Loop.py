from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # Helper function to get the next index in the circular array
        def next_index(i: int) -> int:
            return (i + nums[i]) % len(nums)

        # Step 1: Iterate through each index in the array
        for i in range(len(nums)):
            # Step 2: Check for valid loop, avoiding single-element loops
            if nums[i] == 0:
                continue

            # Step 3: Initialize slow and fast pointers
            slow = i
            fast = next_index(i)

            # Step 4: Loop until we either find a valid loop or invalid condition
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                # Check if the slow pointer and fast pointer meet, indicating a loop
                if slow == fast:
                    # Single-element loop is invalid, so check the length of the loop
                    if slow == next_index(slow):
                        break
                    return True
                
                # Move slow pointer by one step and fast pointer by two steps
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Step 5: Mark all elements in the current traversal as 0 to avoid revisiting
            slow = i
            sign = nums[i]
            while nums[slow] * sign > 0:
                next_slow = next_index(slow)
                nums[slow] = 0  # Mark as visited
                slow = next_slow

        # Step 6: If no valid loop is found, return False
        return False
