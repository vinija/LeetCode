from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the number of binary search iterations
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Handle edge cases where partitionX or partitionY is at the boundary
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total number of elements is odd, return the max of the left side
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    # If even, return the average of the max of left and min of right
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            elif maxLeftX > minRightY:
                # Move the partitionX to the left
                high = partitionX - 1
            else:
                # Move the partitionX to the right
                low = partitionX + 1
        
        raise ValueError("Input arrays are not sorted or not valid.")
