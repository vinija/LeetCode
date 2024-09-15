from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1

        retList = []
        if not nums:
            return [-1,-1]

        while left < right:
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -=1
            
            if nums[left] == target and nums[right] == target:
                return [left, right]
        
        # After loop, left == right
        if left >=0 and left < len(nums) and nums[left] == target:
            return [left, left]
        return [-1, -1]
