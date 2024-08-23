from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() #Sort the array first
        count = 0
        n = len(nums)

        #Iterate over the array and treat each side as the longest
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                #check if sum of smaller two > largest side
                if nums[left] + nums[right] > nums[i]:
                    #If yes, all pairs b/w left and right are valid
                    count += right - left
                    right -= 1 #update right pointer to the left
                else:
                    left += 1 # move the left pointer to the right

        return count
        