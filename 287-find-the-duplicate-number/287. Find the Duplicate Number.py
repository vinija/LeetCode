from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]  # Moves one step
            fast = nums[nums[fast]]  # Moves two steps
            if slow == fast:  # They meet in a cycle
                break

        # Phase 2: Finding the entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Example usage:
sol = Solution()
print(sol.findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(sol.findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
